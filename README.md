# ROCrate_enrichment_service
## AUTHOR: George Hadib

# Introduction:
ROCrate_enrichment_service is a metadata enrichment service for research objects created in RO-Crate format. The service offers a RESTFUL API built with the FLASK library for python. It receives a json/jsonld file and uses the API of the service of OpenAire to asociate more metadata to the original file before it returns another RO-Crate in jsonld format. Signing up to the service is a manual process managed locally by the service provider. Passwords are encrypted using the sha256 algorithm. However, the rest of the operations are available through the public API.

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
The deletion app is an app that runs periodically (every second day) and empties the program's input and owtput folders from unnecessary json files

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
## Deployment:
To run the server make sure to have python3.10 and pip installed in your machine and then follow the following steps:
Step 1 : Clone the repository

`git clone https://github.com/oeg-upm/ROCrate_enrichment_service.git`

Step 2 : Go inside the folder

`cd ROCrate_enrichment_service`

Step 3 : Install requirements

`pip install -r requirements.txt`

Step 4 : Create a new user
. In order to do so, open the script called client.py with a text editor, edit the dictionary called entry_json in line #30 with your username and password and finally run the script. 

Step 5 : Change the SECRET_KEY used to encrypt the passwords to a key of your choice. 
. To do so, open the script called API_Server_v2.py with a text editor and enter the new key in the variable SECRET_KEY in line #10

Step 5 : Run the application

`py run.py`, `py3 run.py`, `python run.py` or `python3 run.py`. This depends on your local environment.



A successful use case of this service is divided in three phases:

## Phase I:
The user sends a json/jsonld file using a POST method to the URI:
`http://domainname.upm.es/api/jobs/`

After receiving the payload, the server responds with status_code of 201 and a ticket in a json payload. This ticket should be collected by the client for it's further use during Phase II.


## Phase II:
The user sends a GET request with the ticket collected from Phase I, the server checks the status of the request involved and responds due to the found results. If the ticket is invalid, the server responds with a 400 status code. If the request is yet to be attended, the server responds with a 200 status code and a "Please try again later" message. If the request is attended and the enriched file is already generated, the server responds with a 200 status code and asks the user to use the GET research_object method to .

## Phase III:
The user sends a GET request woth the tocket and the token to the server. The server basically reapeats the validations of the GET jobs and if everything is fine, it sends the file to the user.

