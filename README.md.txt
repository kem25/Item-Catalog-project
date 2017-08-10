# Item Catalog

Item Catalog is a project that helps to create a web-page that performs CRUD operations using web-services.

## Installation

The project makes use of Linux-based virtual machine (VM). Vagrant and VirtualBox are the two tools you require to install and manage the VM.
VirtualBox is the actual tool that runs the VM. Download and install `VirtualBox`.
Vagrant is the software that configures the VM. Download and Install `Vagrant`.

You can check if vagrant has been installed using 

```sh
$vagrant --version
```

Then downlaod the VM configuration file and change directory to the vagrant file in it.

You can start the VM using 

```sh
$vagrant up
```

Now, run 

```sh
$vagrant ssh 
```
to login to newly installed VM.

Use 

```sh
cd/ vagrant
```
to access files using the vagrant environment

## Required Files

Download or clone the Item-Catalog project. You will find `tdatabase_setup.py`, `populatedb.py`, `application.py`, `tclient_secret.json` and `tfb_clientsecret.json` files.
You will aslo find `static` and `templates` folders.Add all the folders and files to the vagrant folder. 

## Database Connection

Change directory to the folder which contains project in the vagrant in the git bash command prompt. 

First run,
```sh
python tdatabase_setup.py
```
to set up the database connection.

Then run,
```sh
python populatedb.py
```
to populate the database.

Now run,
```sh
python application.py
```
to run the application.

## Accessing the webpage

Now open browser and visit the localhost port where our application runs
```sh
http://localhost:5000/
```

### View

You will be taken to the home page. You can navigate between different pages using the buttons provided in the page.

## Using the application

You can navigate to view the country and places belonging to each country. To add your own items you need to login using the login option(facebook/googleplus).
Logout when done with the changes.