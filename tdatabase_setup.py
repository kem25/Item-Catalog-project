import sys
from sqlalchemy import Column,ForeignKey,Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base=declarative_base()

class User(Base):
    __tablename__='user'
    name=Column(String(250),nullable=False)
    id=Column(Integer,primary_key=True)
    email=Column(String(250),nullable=False)
    picture=Column(String(250))

class Country(Base):
    __tablename__='country'
    name=Column(String(80),nullable=False)
    id=Column(Integer, primary_key=True)
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship(User)
    
    @property
    def serialize(self):
        return{
            'name':self.name,
            'id':self.id
            }
    
class VisitList(Base):
    __tablename__='visit_list'
    name=Column(String(80),nullable=False)
    id=Column(Integer,primary_key=True)
    country_id=Column(Integer,ForeignKey('country.id'))
    country=relationship(Country)
    description=Column(String(500))
    category=Column(String(40))
    besttime=Column(String(40))
    user_id=Column(Integer,ForeignKey('user.id'))
    user=relationship(User)

    @property
    def serialize(self):
        return{
            'name':self.name,
            'id':self.id,
            'description':self.description,
            'category':self.category
            }
            

engine=create_engine('sqlite:///catalog3.db')

Base.metadata.create_all(engine)

