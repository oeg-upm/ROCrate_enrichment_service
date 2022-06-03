from pydoc import resolve
from flask import Flask, request, jsonify, send_file
from flask_restful import Api, Resource
import os, uuid, jwt, json
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3 as sql
from werkzeug.datastructures import ImmutableMultiDict




UPLOAD_FOLDER = '/pending_jobs'
DOWNLOAD_FOLDER = '/done_jobs'
SECRET_KEY = 'UPMROCRATEENRICHMENTSERVICE'
ALLOWED_EXTENSIONS = {'json', 'jsonld'}
CURRENT_USER = {}

# Start the flask API app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
api = Api(app)

def allowed_file(filename):
    	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
def token_authentication (token):
    data = jwt.decode(token, app.config['SECRET_KEY'], "HS256")
    id = data.get("id")
    conn = sql.connect("Database/enrrichmentDB.db")
    cursor = conn.cursor()
    instruction = f"SELECT 1 FROM users WHERE id = '{id}'"
    result = cursor.execute(instruction)
    if result:
        CURRENT_USER = result
        return True
    return False

def check_status (ticket: str):
    conn = sql.connect("Database/enrrichmentDB.db")
    cursor = conn.cursor()
    print(ticket)
    instruction = f"SELECT EXISTS (SELECT 1 FROM jobs WHERE job_id = '4cdd03f7-eebc-4597-9469-2325aa17cc94')"
    
    exists = cursor.execute(instruction).fetchone()[0]
    if exists < 0:
        return (-1)
    else:
        instruction = f"SELECT EXISTS (SELECT 1 FROM jobs WHERE job_id = '{ticket}' AND ready = TRUE)"
        ready = cursor.execute(instruction).fetchone()[0]
        if ready > 0:
            return 1    
        return 0  

    
   

class Jobs (Resource):
    def post(self):
        token = json.loads(request.form.to_dict(flat=False).get('token')[0]).get("token")
        authorized = token_authentication(token)
        if authorized:
            if 'file' not in request.files:
                resp = jsonify({'message' : 'No file part in the request. Please make sure to upload the json/jsonld file.'})
                resp.status_code = 400
                return resp
            
            file = request.files['file']
            
            if file.filename == '':
                resp = jsonify({'message' : 'No file selected for uploading. Please make sure to upload the json/jsonld file.'})
                resp.status_code = 400
                return resp
            if file and allowed_file(file.filename):
                filename = str(uuid.uuid4())+'.'+file.filename.rsplit('.', 1)[1].lower()
                if not os.path.exists(app.config['UPLOAD_FOLDER']):
                    os.makedirs(app.config['UPLOAD_FOLDER'])

                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                ticket = filename.rsplit('.', 1)[0].lower()
                
                if not os.path.exists("Database"):
                    os.makedirs("Database")
                conn = sql.connect("Database/enrrichmentDB.db")
                cursor = conn.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS jobs (job_id text NOT NULL, client text NOT NULL, ready boolean NOT NULL)""")
                instruction = f"INSERT INTO jobs VALUES ('{ticket}','sdfafaf',FALSE)"
                cursor.execute(instruction)
                conn.commit()
                conn.close
                
                resp = jsonify({'message' : 'File successfully uploaded',
                                'ticket' : ticket})
                resp.status_code = 201
                return resp

            else:
                resp = jsonify({'message' : 'Please make sure to upload a valid file type. Allowed file types are json and jsonld'})
                resp.status_code = 400
                return resp
        else:
            resp = jsonify({'message' : 'You are not allowed to perform this request. Please make sure that you are logged in to the service.'})
            resp.status_code = 400
            return resp

    def get(self):
        if not request.json:
            resp = jsonify({'message' : 'Please make sure to send a valid request. Your request lacks a json payload.'})
            resp.status_code = 400
            return resp    
        if not "ticket" in request.json:
            resp = jsonify({'message' : 'Please make sure to send a valid request. Your json payload lacks a ticket key'})
            resp.status_code = 400
            return resp 
        else:
            ticket = request.json.get("ticket")
            result = check_status(ticket)
            if result == -1:
                resp = jsonify({'message' : 'Please make sure to send a valid request. Your json payload has an invalid ticket'})
                resp.status_code = 400
                return resp   
            if result == 0:
                resp = jsonify({'message' : 'Your request is yet to be attended. Please try again in a few minutes'})
                resp.status_code = 200
                return resp
            else:   
                resp = jsonify({'message' : 'Your request is ready. Please use your ticket to request your file from http://hostname.upm.es/api/research_object/'})
                resp.status_code = 200
                return resp


class login(Resource):
    def post(self):
        if 'username' not in request.json or 'userpassword' not in request.json:
            resp = jsonify ({'message' : 'Please make sure to send a valid request. Your request is missing a username and/or a password'})
            resp.status_code = 401
            return resp
        entry_dict = request.json
        conn = sql.connect("Database/enrrichmentDB.db")
        cursor = conn.cursor()
        username = entry_dict.get("username")
        
        
        instruction = f"SELECT * FROM users WHERE username = '{username}'"
        result = cursor.execute (instruction)
        for user in result.fetchall():
            print(user[2])
            if check_password_hash(user[2],entry_dict.get("userpassword")):
                CURRENT_USER = user
                token = jwt.encode({'id':user[0]}, SECRET_KEY, "HS256")
                resp = jsonify ({'message':'Logged in successfully. Please recover your token', 'token':token})
                resp.status_code = 200
                conn.close()

                return resp
            else:
                resp = jsonify ({'message' : 'Login request declined! Please make sure to send a valid username and password'})
                resp.status_code = 401
                return resp
            
class research_object (Resource):
    def get(self):
        authorized = token_authentication(request.json.get('token'))
        if authorized:
            if 'file' not in request.files:
                resp = jsonify({'message' : 'No file part in the request. Please make sure to upload the json/jsonld file.'})
                resp.status_code = 400
                return resp

            if not "ticket" in request.json:
                resp = jsonify({'message' : 'Please make sure to send a valid request. Your json payload lacks a ticket key'})
                resp.status_code = 400
                return resp 
            else:
                ticket = request.json.get("ticket")
                status = check_status(ticket)
                if status == 1:
                    resp = send_file(app.config['DOWNLOAD_FOLDER'] + '/' + ticket+".jsonld", attachment_filename="lksjdlad")
                    resp.status_code = 200
                    return resp
                else:
                    resp = jsonify({'message' : 'Couldn\' download file. Your file isn\'t ready yet.'})
                    resp.status_code = 400
                    return resp 

        else:
            resp = jsonify({'message' : 'You are not allowed to perform this request. Please make sure that you are logged in to the service.'})
            resp.status_code = 400
            return resp

                
def signup(entry_dict:dict):
    entry_dict = {'username':'user1','userpassword':'password123'}
    conn = sql.connect("Database/enrrichmentDB.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE users;")
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id text NOT NULL UNIQUE PRIMARY KEY,
    username text NOT NULL, 
    userpassword text NOT NULL,
    admin boolean DEFAULT 0)""")
    username = entry_dict.get("username")
    userpassword = generate_password_hash(entry_dict.get("userpassword"), method= 'sha256')
    id = str(uuid.uuid4())
    instruction = f"INSERT INTO users VALUES ('{id}','{username}','{userpassword}', 0)"
    result = cursor.execute(instruction)
    conn.commit()
    conn.close()
    if result:
        return jsonify({'message':'New user was created'}), 201
    return jsonify({'message' : 'Something went wrong. Please make sure to enter both username and password.'}), 401


'''
def login (entry_dict: dict):
  conn = sql.connect("Database/enrrichmentDB.db")
  cursor = conn.cursor()
  username = entry_dict.get("username")
  userpassword = generate_password_hash(entry_dict.get("userpassword"))
  instruction = f"SELECT 1 FROM users WHERE username = '{username}' AND userpassword = '{userpassword}'"
  result = cursor.execute (instruction)
  conn.commit()
  conn.close()
  if result:
    CURRENT_USER = result
    token = jwt.encode({'id':result.get('id')}, SECRET_KEY)
    return token
  else:
    return null
    '''    





api.add_resource(Jobs,"/api/jobs/")
api.add_resource(login,"/api/login/")
api.add_resource(research_object, "/api/research_object/")

# Execution

if __name__ == "__main__":
    app.run(debug=True)



