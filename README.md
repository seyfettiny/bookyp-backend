## Features

- Retrieve JSON responses with defined models.
- JSON Web Token Authorization.
- SMTP mail operations on local.
- MongoDB integration with [mongoengine](http://mongoengine.org/).
- Password encryption with bcrypt.



------------



## Usage

**Install Python [here](https://www.python.org/downloads/)**
**Install MongoDB [here](https://www.mongodb.com/download)**


**Activate pipenv shell at root project directory;**

	pipenv shell


**Install requirements defined in Pipfile**

	pipenv install


**After installation you should create a .env file at root project directory**

	JWT_SECRET_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE2MjMwODQwNTYsImV4cCI6MTYyMzA4NDA2NCwiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcG' 
	MAIL_SERVER = "localhost" 
	MAIL_PORT = "1025" 
	MAIL_USERNAME = "support@mail.com" 
	MAIL_PASSWORD = "123" 
	PORT = 8000 

**Export .env file as environment variable**

	//for linux
	export ENV_FILE_LOCATION=./.env
	
	//for windows
	set ENV_FILE_LOCATION=./.env

**Run the app**

	python main.py

**And you should see something like this**

	(bookyp-backend-aCPFcfJr) C:\bookyp-backend>python main.py
	 * Serving Flask app 'app' (lazy loading)
	 * Environment: production
	   WARNING: This is a development server. Do not use it in a production deployment.
	   Use a production WSGI server instead.
	 * Debug mode: off
	 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

**Run following command on another terminal to run mail server**

	python -m smtpd -n -c DebuggingServer localhost:1025
	
------------



### All contributions are welcomed!

