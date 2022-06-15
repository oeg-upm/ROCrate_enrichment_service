# ROCrate_enrichment_service
## AUTHOR: George Hadib

# Introduction:
ROCrate_enrichment_service is a metadata enrichment service for research objects created in RO-Crate format. The service offers a RESTFUL API built with the FLASK library for python. It receives a json/jsonld file and uses the API of the service of OpenAire to asociate more metadata to the original file before it returns another RO-Crate in jsonld format. Signing up to the service is a manual process managed locally by the service provider. Passwords are encrypted using the sha256 algorithm. However, the rest of the operations are available through the public API.

# Database:
The following diagram represents the database used in this project:

![image](https://user-images.githubusercontent.com/17781274/172913965-6cac0d06-232d-4b74-9806-18e1df234d89.png)

The databse was built with SQLite and contains two tables:
## users:
This table contains the authorized users of the service. The primary key of an entry is the id which is an unique id created by the uuid functionality.
Passwords are hashed with sha256 before being saved in the database
admin is 0 by default

## jobs:
This table contains the jobs that are uploaded to the service, their original name, their owner and their status.
job_id is the primary key and as for users it's created by uuid. This same uuid is used for the temporary naming of the uploaded files.
The original name of the uploaded file is saved in order to use it again for the download
client is a foreign key inherited from the users table and refers to the owner of a job
A value of 1 in the ready column means that the RO was enriched and a 0 means that it's yet to be enriched

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

# Deletion App:
The deletion app is an app that runs periodically (every second day) and empties the project folders from unnecessary json files

# The API:
The project has a restful API designed with flask on python. The API has 3 resources that will be explained afterwards:

## login:
Path: `/api/login/`

Available methods: POST

This operation receives the username and password and compare them to the username and encrypted password saved in the database. This operation requires a json payload that must have the next format:
`{"username":"valid_username", "userpassword":"valid_password"}`

The login method returns a json payload with a token. The token should be collected for it's further use in other operations. The json payload has the next format:
`{"token":"valid_user_token"}`

## jobs:
Path: `/api/jobs/`

Available methods: GET, POST

POST jobs:
This method receives a formadata payload. The payload should have a json/jsonld file in a RO-Crate format and a json with the next format:
`{"token":"valid_user_token"}`
After receiving the payload, the method checks the authentication of the token using the local methid "token_authentication (token)", saves the file in the upload folder, inserts a job in the jobs table of the database and returns a tracing tickit that should be used later in other operations. The ticket is returned in a json payload with the following format:
`{"ticket":"valid_ticket"}`

GET jobs:
This method receives the token of the user and a given ticket to trace the uploaded job. The json received payload should have the following format:
`{"token":"valid_user_token","ticket":"valid_ticket"}`
After receiving the input payload this method compares with the saved jobs in the database to make sure that only file owners can check the status of their files before responding. Afterwards, the get method returns the status of the request. Posible status messages are no valid token/ticket message, Ownershp error message, pending status message and ready status message. Messages are sent in a json payload with the next format:
`{"message":"status message"}`

## research_object:
Path: `/api/research_object/`

Available methods: GET

This get method receives a json payload with the following format:
`{"token":"valid_user_token","ticket":"valid_ticket"}`
When the payload is received, the method has a similar behavior to the GET jobs method. In other words, it makes sure that the user is authorized, the ticket is valid, the ticket belongs to the same user and finally that the status is set to "ready". After the verification, the method sends the new file to the user.


# How to use?
## Requirements:
To run the server make sure to have python3.10 and pip installed in your machine and then follow the following steps:
Step 1 : Clone the repository
`git clone https://github.com/oeg-upm/ROCrate_enrichment_service.git`

Step 2 : Go inside the folder
`cd ROCrate_enrichment_service`

Step 3 : Install requirements
pip install -r requirements.txt *this might take a while

Step 4 : Run the application
python run.py



A successful use case of this service is divided in three phases:

## Phase I:
The user sends a json/jsonld file using a POST method to the URI:
`http://domainname.upm.es/api/jobs/`

After receiving the payload, the server responds with status_code of 201 and a ticket in a json payload. This ticket should be collected by the client for it's further use during Phase II.


## Phase II:
The user sends a GET request with the ticket collected from Phase I, the server checks the status of the request involved and responds due to the found results. If the ticket is invalid, the server responds with a 400 status code. If the request is yet to be attended, the server responds with a 200 status code and a "Please try again later" message. If the request is attended and the enriched file is already generated, the server responds with a 200 status code and asks the user to use the GET research_object method to .

## Phase III:
The user sends a GET request woth the tocket and the token to the server. The server basically reapeats the validations of the GET jobs and if everything is fine, it sends the file to the user.

