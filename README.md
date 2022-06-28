# ROCrate_enrichment_service
## AUTHOR: George Hadib

# Introduction:
ROCrate_enrichment_service is a metadata enrichment service for research objects created in RO-Crate format. The service offers a RESTFUL API built with the FLASK library for python. It receives a json/jsonld file and uses the API of the service of OpenAire to associate more metadata to the original file before it returns another RO-Crate in jsonld format. Signing up to the service is a manual process managed locally by the service provider. Passwords are encrypted using the sha256 algorithm. However, the rest of the operations are available through the public API.

# Enrichment App:
The enrichment app is the core of this project. It's an app that infinitively and periodically does the following sequence of operations:

![image](https://user-images.githubusercontent.com/17781274/172907425-faf5dcce-1f43-41df-b6f3-228f088ac7a6.png)


1. Checks for pending jobs in the database.

  Steps 2 to 5 are only followed if there are some pending jobs:
  
    2. The app recovers the corresponding file from the INPUT_FOLDER (The same as the API upload folder)
    3. The app then enriches the RO-Crate using the OpenAire service
    4. The result is saved in the OUTPUT_FOLDER (The same as the API download folder)
    5. The database is updated and the status of the fulfilled requests is set to ready
 6. The app sleeps during one minute and then returns to step 1.


# The API:
The project has a restful API designed with flask-restful on python. The API has a JWT authentication system and 4 resources that will be explained afterwards:

## Swagger:

`https://app.swaggerhub.com/apis/GHADIB_1/restful-api_ro_enrichment/2.0.0`

## token_required decorator:
This decorator is used in the authentication system and is in charge of authenticating JWT tokens and grant or decline access to the service based on the obtained result.

## login Resource:
Path: `/api/login/`

Available methods: POST

This operation receives the username and password and compare them to the username and encrypted password saved in the database. This operation requires a json payload that must have the next format:
`{"username":"valid_username", "userpassword":"valid_password"}`

The login method returns a json payload with a token. The token should be collected for it's further use in other operations. The json payload has the next format:
`{"token":"valid_user_token"}`

## jobs Resource:
Path: `/api/jobs/`

Available methods: GET, POST

@token_required
POST jobs:
This method receives a formadata payload. The payload should have a json/jsonld file in a RO-Crate format..

The @token_required decorator controls access to this method. The method saves the file in the upload folder, inserts a job in the jobs table of the database and returns a tracing ticket that should be used later in other operations. The ticket is returned in a json payload with the following format:
`{"ticket":"valid_ticket"}`

@token_required
GET jobs:
This method receives no payload. Based on the token delivered in the header, it navigates in the database and returns to the user a list of all the pending jobs belonging to the involved user. The response of this request is a json that contains a list of lists as in the following example:

`{"results":[ ["ticket_1", "file_original_name_1", "user_id", ready/not ready], ["ticket_2", "file_original_name_2", "user_id", ready/not ready], .... ]}`


## job Resource:
Path: `/api/job/<ticket>/`

Available methods: GET

@token_required
Get job:
The @token_required decorator controls access to this method. This method also receives ticket of the job which the user wants to consult. The method then consult the database and only returns the status of the job to its owner. In case of a ready job, the method returns, as well, the link that can be used to download the enriched RO.

`{"message":"status message", "link":"download_link"}`


## research_object Resource:
Path: `/api/research_object/<ticket>`

Available methods: GET

@token_required
Get research_object:
The @token_required decorator controls access to this method. This method also receives ticket of the job which the user wants to download. The method then consult the database and only sends the file to its owner.

# Support scripts:
## deletion.py:
This method takes care of emptying the input and output folder of the server to remove all unnecessary files. You can execute it manually or program it to be launched by another process periodically

## sign_up.py:
This method signs a user up in the service. It receives arguments in the in the command line and in a successful scenario, it creates an entry in the users table in the database. Otherwise, it returns an error message to stdout. An example of how to use the method can be:

`py sign_up.py Username123 Password123`

## drop.py:
This script was created for testing. It drops all the tables in the database.

## create_db.py:
This script creates the database manually. It should be used in a manual deployment scenario.

# More folders and files:
## Database:
As its name indicates. This folder hosts the database used in this project called enrichmentDB.db

## pending_jobs & done_jobs:
These folders host the RO-Crate files sent by the users. When the files uploaded the service, they are hosted in the pending_jobs folder. When the enrichment core processes a request, it saves the enriched file in the done_jobs folder. The API then sends the enriched file to the user.
These folders are emptied periodically by the deletion script.

## log:
This folder hosts the log files of the service. Log files are created daily and save relevant data.

## Dockerfile:
This file contains the descriptions of the docker image that is used to create the container.

## swagger.yaml:
This file contains the description of the API and it’s used to create the swagger documentation of the API:

`https://app.swaggerhub.com/apis/GHADIB_1/restful-api_ro_enrichment/2.0.0#/`

## requirements.txt:
This file contains the python libraries that should be installed to deploy the service successfully. It’s used in the deployment process to create the environment.

## LICENSE:
A public apache license for the project.


# How to use?
## Deployment:
There are two deployment methods. Dockerized and manual. In the following chapter you can find the deployment instructions:

Dockerized deployment:
Step 1 : Clone the repository

`git clone https://github.com/oeg-upm/ROCrate_enrichment_service.git`

Step 2 : Install docker in your machine. For more information, visit the webpage:

`https://docs.docker.com/get-docker/`

Step 3 : In your CMD/terminal navigate to the project folder and build the docker container using the command:

`cd ROCrate_enrichment_service`

`docker build -t python-flask .`

Step 4 : Run the container by executing the next command after changing the variable [PORT_NUM] with the port to which you want the API to listen:

`docker run -p [PORT_NUM]:5000 python-flask`


Manual deployment:
Please note that this deployment method is vulnerable to environment changes. To run the server make sure to have python3.10 and pip installed in your machine and then follow the following steps:


Step 1 : Clone the repository

`git clone https://github.com/oeg-upm/ROCrate_enrichment_service.git`

Step 2 : Go inside the project folder

`cd ROCrate_enrichment_service`

Step 3 : Install requirements

`pip install -r requirements.txt`

Step 4 : Create a new user
. In order to do so, open the script called client.py with a text editor, edit the dictionary called entry_json in line #30 with your username and password and finally run the script. 

Step 5 : Change the SECRET_KEY used to encrypt the passwords to a key of your choice. 
. To do so, open the script called API_Server_v2.py with a text editor and enter the new key in the variable SECRET_KEY in line #10

Only if you are using linux:
  
  Step 6 : Run the application on your linux machine

  `py run.py`, `py3 run.py`, `python run.py` or `python3 run.py`. This depends on your local environment. 

If you are not using linux, follow steps 6-9:
  
  Step 6: Create the database and it's tables by executing the script called create_db.py through the following command

  `py create_db.py`

  Step 7: Run the scripts API_Server_v2.py and enrichment.py by using the following commands

  `py enrichment.py` and `py API_Server_v2.py`

  Step 8: Use the cron functions to run the script deletion.py periodically
A successful use case of this service is divided in five phases:

## Phase I
The user sends a login POST request to the system providing a valid pair of credentials. The system responds with a valid token and a status code 200. 


## Phase II:
The user uses the provided token and sends a json/jsonld file using a POST method to the URI:
`http://domainname.upm.es/api/jobs/`

After receiving the payload, the server responds with status_code of 201 and a ticket in a json payload. This ticket should be collected by the client for it's further use during Phase II.

## Phase III:
The user sends a jobs Get request to the system. The system responds with a list of all the jobs that the user had requested and their status.

## Phase IV:
The user sends a job GET request with the ticket collected from Phase I, the server checks the status of the request involved and responds due to the found results. If the ticket is invalid, the server responds with a 400 status code. If the request is yet to be attended, the server responds with a 200 status code and a "Please try again later" message. If the request is attended and the enriched file is already generated, the server responds with a 200 status code and asks the user to use the GET research_object method to download tha enriched RO-Crate.

## Phase V:
The user sends a GET request with the ticket and the token to the server. The server basically repeats the validations of the GET jobs and if everything is fine, it sends the file to the user.

