from sqlalchemy import create_engine, asc, desc
from sqlalchemy.orm import sessionmaker
from tdatabase_setup import Base, Country, VisitList, User
import random
import string
from flask import session as login_session
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests
import os
from flask import Flask, render_template, url_for 
from flask import redirect, request, flash, jsonify


# reading client_id from json file
CLIENT_ID = json.loads(
    open('tclient_secret.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "itemcatalog"

# connecting to the database and session initisiation
engine = create_engine('sqlite:///catalog4.db',
                       connect_args={'check_same_thread': False})
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)

# code for login-module and generation of state variable
@app.route('/login/')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return state
    return render_template('tlogin.html',
                           STATE=state, login_session=login_session)

# facebook login
@app.route('/fbconnect', methods=['POST'])
def fbconnect():
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = request.data
    print "access token received %s " % access_token
    app_id = json.loads(open('tfb_client_secret.json', 'r').read())[
        'web']['app_id']
    app_secret = json.loads(
        open('tfb_client_secret.json', 'r').read())['web']['app_secret']
    url = 'https://graph.facebook.com/oauth/access_token?grant_type=fb_exchange_token&client_id=%s&client_secret=%s&fb_exchange_token=%s' % (
        app_id, app_secret, access_token)
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]

    # Use token to get user info from API
    userinfo_url = "https://graph.facebook.com/v2.8/me"
    '''
        Due to the formatting for the result from the server token exchange
        we have to split the token first on commas and select the
        first index which gives us the key : value for the server access
        token then we split it on colons to pull out the actual token value
        and replace the remaining quotes with nothing so that it can be used
        directly in the graph api calls
    '''
    token = result.split(',')[0].split(':')[1].replace('"', '')

    url = 'https://graph.facebook.com/v2.8/me?access_token=%s&fields=name,id,email' % token  # noqa
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    # print "url sent for API access:%s"% url
    # print "API JSON result: %s" % result
    data = json.loads(result)
    login_session['provider'] = 'facebook'
    login_session['username'] = data["name"]
    login_session['email'] = data["email"]
    login_session['facebook_id'] = data["id"]

    # The token must be stored in the login_session in order to properly logout
    login_session['access_token'] = token

    # Get user picture
    url = 'https://graph.facebook.com/v2.8/me/picture?access_token=%s&redirect=0&height=200&width=200'  % token  # noqa
    h = httplib2.Http()
    result = h.request(url, 'GET')[1]
    data = json.loads(result)

    login_session['picture'] = data["data"]["url"]

    # see if user exists
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']

    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '  # noqa

    flash("Now logged in as %s" % login_session['username'])
    return output


# facebook logout
@app.route('/fbdisconnect')
def fbdisconnect():
    facebook_id = login_session['facebook_id']
    # The access token must me included to successfully logout
    access_token = login_session['access_token']
    url = 'https://graph.facebook.com/%s/permissions?access_token=%s' % (facebook_id, access_token)  # noqa
    h = httplib2.Http()
    result = h.request(url, 'DELETE')[1]
    return "you have been logged out"


# google login
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('tclient_secret.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps
                                 ('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = 'gplus_id'

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    # login_session['gplus_id']= data['gplus_id']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    login_session['provider'] = 'google'

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += ' " style = "width: 300px; height: 300px;border-radius: 150px;-webkit-border-radius: 150px;-moz-border-radius: 150px;"> '   # noqa
    flash("you are now logged in as %s" % login_session['username'])
    print "done!"
    return output

# google logout
@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps
                                 ('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print 'In gdisconnect access token is %s', access_token
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s'% login_session[
        'access_token']
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps
                                 ('Failed to revoke token for given user.',
                                  400))
        response.headers['Content-Type'] = 'application/json'
        return response


# JSON APIs to view Country information
@app.route('/catalog/<string:countryname>/JSON')
def RplacesJSON(countryname):
    c1 = session.query(Country).filter_by(name=countryname).one()
    c2 = session.query(VisitList).filter_by(country_id=c1.id).all()
    return jsonify(c2=[i.serialize for i in c2])


# JSON API to view place information
@app.route('/catalog/<string:countryname>/<string:placename>/JSON')
def countryplaceJSON(countryname, placename):
    place1 = session.query(VisitList).filter_by(name=placename).one()
    return jsonify(place1=[place1.serialize])


# JSON API to view all Countries
@app.route('/catalog/JSON')
def catalogJSON():
    countries = session.query(Country).all()
    return jsonify(countries=[r.serialize for r in countries])


# mapping homepage
@app.route("/")
@app.route("/catalog/")
def homepage():
    CountryList = session.query(Country).all()
    latestList = session.query(VisitList).order_by(desc('id')).limit(7)
    return render_template('homepage.html', CountryList=CountryList,
                           latestList=latestList, login_session=login_session)


# mapping for viewing country itmes
@app.route('/catalog/<string:countryname>/')
def displayitems(countryname):
    CountryList = session.query(Country).all()
    SelectedCountry = session.query(Country).filter_by(name=countryname).one()
    Items = session.query(VisitList).filter_by(
    country_id=SelectedCountry.id).all()
    rows = session.query(VisitList).filter_by(
    country_id=SelectedCountry.id).count()
    return render_template('items.html', SelectedCountry=SelectedCountry,
                           Items=Items, countryname=countryname,
                           CountryList=CountryList,
                           login_session=login_session, rows=rows)


# mapping for adding new item
@app.route('/catalog/<string:countryname>/additem', methods=['POST', 'GET'])
def additem(countryname):
    if 'username' not in login_session:
        return redirect('/login')
    currentCountry = session.query(Country).filter_by(name=countryname).one()
    if request.method == 'POST':
        newItem = VisitList(name=request.form['name'],
                            description=request.form['description'],
                            country_id=currentCountry.id,
                            category=request.form['category'])
        session.add(newItem)
        session.commit()

        return redirect(url_for('displayitems',
                        countryname=countryname,
                        login_session=login_session))

    else:
        return render_template('addplace.html',
                               currentCountry=currentCountry,
                               countryname=countryname,
                               login_session=login_session)


# mapping for viewing place info 
@app.route('/catalog/<string:countryname>/<string:placename>/')
def viewinfo(countryname, placename):
    getplace = session.query(VisitList).filter_by(name=placename).one()
    return render_template('viewinfo.html',
                           getplace=getplace, countryname=countryname,
                           placename=placename, login_session=login_session)


# mapping for editing the place info
@app.route('/catalog/<string:countryname>/<string:placename>/edit/', methods=['GET', 'POST'])  # noqa
def editinfo(countryname, placename):
    if 'username' not in login_session:
        return redirect('/login')
    countryselect = session.query(Country).filter_by(name=countryname).one()
    editItem = session.query(VisitList).filter_by(name=placename).one()
    origItem = session.query(VisitList).filter_by(id=editItem.id).one()
    if request.method == 'POST':
        
        if request.form['name']:
            editItem.name = request.form['name']
        else:
            editItem.name=origItem.name
        if request.form['description']:
            editItem.description = request.form['description']
        else:    
            editItem.description=origItem.description
        if request.form['category']:
            editItem.categeory = request.form['category']
        else:    
            editItem.category=origItem.category
        session.add(editItem)
        session.commit()
        placename=request.form['name']
        return redirect(url_for('displayitems',countryname=countryselect.name))
    else:
        return render_template('editinfo.html',
                               countryname=countryselect.name,
                               placename=editItem.name,
                               editItem=editItem,
                               login_session=login_session)


# mapping for deleting place info
@app.route('/catalog/<string:countryname>/<string:placename>/delete/', methods=['GET', 'POST'])  # noqa
def delinfo(countryname, placename):
    if 'username' not in login_session:
        return redirect('/login')
    cselect = session.query(Country).filter_by(name=countryname).one()
    delItem = session.query(VisitList).filter_by(name=placename).one()
    if request.method == 'POST':
        session.delete(delItem)
        session.commit()
        return redirect(url_for('displayitems', countryname=countryname))
    else:
        return render_template('del.html', countryname=cselect.name,
                               placename=delItem.name, delItem=delItem,
                               login_session=login_session)


# user info functions
def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None


def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


def createUser(login_session):
    newUser = User(name=login_session['username'],
                   email=login_session['email'],
                   picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


# disconnectiong from login session and revoking tokens 
@app.route('/disconnect')
def disconnect():
    if 'provider' in login_session:
        if login_session['provider'] == 'google':
            gdisconnect()
            # del login_session['gplus_id']
            # del login_session['credentials']
        if login_session['provider'] == 'facebook':
            fbdisconnect()
            del login_session['facebook_id']
            del login_session['username']
            del login_session['email']
            del login_session['picture']
            del login_session['user_id']
            del login_session['provider']
        flash("You have successfully been logged out.")
        return redirect(url_for('homepage'))
    else:
        flash("You were not logged in")
        return redirect(url_for('homepage'))


# calling main
if __name__ == '__main__':
    app.secret_key = 'super_secret_keys'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
