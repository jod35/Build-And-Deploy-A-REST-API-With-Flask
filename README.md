# Build And Deploy A REST API with Flask
This is code for a series of videos in which we look at the various concepts involved when building a REST API with Flask. We also look at the various extensions involved while building Flask applications.

## Topics
- [How to set up a Flask API with Flask-RESTX]
- Databases with Flask-SQLAlchemy
- JWT Authentication with Flask-JWT-Extended
- Environment variables with Python-Decouple
- Database migrations with Flask-Migrate
- How to write Unit Tests with Unittest and PyTest
- Documenting REST APIs with SwaggerUI and Flask-RESTX
- Error Handling with Werkzeug

 

## How to run the project

Clone the project Repository
```
git clone https://github.com/jod35/Buildndeploy-A-REST-API-With-Flask.git

```

Enter the project folder and create a virtual environment
``` 
$ cd https://github.com/jod35/Build-And-Deploy-A-REST-API-With-Flask 

$ python -m venv env 

```

Activate the virtual environment
``` 
$ source env/bin/actvate #On linux Or Unix

$ source env/Scripts/activate #On Windows 
 
```

Install all requirements

```
$ pip install -r requirements.txt
```

Run the project in development
```
$ export FLASK_APP=api/

$ export FLASK_DEBUG=1

$ flask run

```
Or 
``` 
python runserver.py
``` 

