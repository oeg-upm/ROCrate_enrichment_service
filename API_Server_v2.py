from flask import Flask, request, jsonify, send_file
from flask_restful import Api, Resource
import os, uuid, jwt, json, time, datetime as dt, sqlite3 as sql
from werkzeug.security import generate_password_hash, check_password_hash




UPLOAD_FOLDER = './pending_jobs'
DOWNLOAD_FOLDER = './done_jobs'
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
    try:
        data = jwt.decode(token, app.config['SECRET_KEY'], "HS256")
    except:
        return False    
    id = data.get("id")
    
    conn = sql.connect("./Database/enrrichmentDB.db")
    cursor = conn.cursor()
   
    instruction = f"SELECT username FROM users WHERE id = '{id}'"
    result = cursor.execute(instruction).fetchone()
    if result:
        CURRENT_USER = result
        return result[0]
    return False

def check_status (ticket: str, token: str):
    conn = sql.connect("./Database/enrrichmentDB.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM jobs WHERE job_id = '{ticket}'"
    
    result = cursor.execute(instruction).fetchone()

    
    if not result:
        return (-1)
    else:
        if result[2] == token:
            ready = result[3]
            if ready > 0:
                return result[1]    
            return 0  
        else:
            return -2
    
   

class Jobs (Resource):
    def post(self):
        token = json.loads(request.form.to_dict(flat=False).get('token')[0]).get("token")
        conn = sql.connect("./Database/enrrichmentDB.db")
        
        user = token_authentication(token)
        if user:
            if 'file' not in request.files:
                message = 'No file part in the request. Please make sure to upload the json/jsonld file.'
                resp = jsonify({'message' : message})
                resp.status_code = 400
                today = str(dt.date.today())
                if not os.path.exists("log"):
                    os.makedirs("log")
                log_file = open("./log/log-"+today+".txt", "a")
                log_time = time.localtime()
                log_time = time.strftime("%H:%M:%S", log_time)
                
                
                log = f"************************************************\n{log_time}: The user with the username: '{user}' made a job post request without attaching any file.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                log_file.writelines(log)            
                log_file.close()
                return resp
            
            file = request.files['file']
            
            if file.filename == '':
                message = 'No file selected for uploading. Please make sure to upload the json/jsonld file.'
                
                resp = jsonify({'message' : message})
                resp.status_code = 400
                today = str(dt.date.today())
                if not os.path.exists("log"):
                    os.makedirs("log")
                log_file = open("./log/log-"+today+".txt", "a")
                log_time = time.localtime()
                log_time = time.strftime("%H:%M:%S", log_time)
                log = f"************************************************\n{log_time}: The user with the username: '{user}' made a job post request without attaching any file.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                log_file.writelines(log)            
                log_file.close()
                return resp

            if file and allowed_file(file.filename):
                filename = str(uuid.uuid4())+'.'+file.filename.rsplit('.', 1)[1].lower()
                if not os.path.exists(app.config['UPLOAD_FOLDER']):
                    os.makedirs(app.config['UPLOAD_FOLDER'])

                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                ticket = filename.rsplit('.', 1)[0].lower()
                
                if not os.path.exists("Database"):
                    os.makedirs("Database")
                conn = sql.connect("./Database/enrrichmentDB.db")
                cursor = conn.cursor()                
                cursor.execute("""CREATE TABLE IF NOT EXISTS jobs (job_id text NOT NULL, original_name text NOT NULL, client text NOT NULL, ready boolean NOT NULL)""")
                instruction = f"INSERT INTO jobs VALUES ('{ticket}','{file.filename}','{token}',FALSE)"
                cursor.execute(instruction)
                conn.commit()
                conn.close
                message = 'File successfully uploaded. Please recover your ticket: '+ ticket
                resp = jsonify({'message' : message, 'ticket' : ticket})
                resp.status_code = 201
                today = str(dt.date.today())
                if not os.path.exists("log"):
                    os.makedirs("log")
                log_file = open("./log/log-"+today+".txt", "a")
                log_time = time.localtime()
                log_time = time.strftime("%H:%M:%S", log_time)
                log = f"************************************************\n{log_time}: The user with the username: '{user}' made a successfull job post request.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                log_file.writelines(log)            
                log_file.close()
                return resp

            else:
                message = 'Please make sure to upload a valid file type. Allowed file types are json and jsonld'
                resp = jsonify({'message' : message})
                resp.status_code = 400
                today = str(dt.date.today())
                if not os.path.exists("log"):
                    os.makedirs("log")
                log_file = open("./log/log-"+today+".txt", "a")
                log_time = time.localtime()
                log_time = time.strftime("%H:%M:%S", log_time)
                log = f"************************************************\n{log_time}: The user with the username: '{user}' made a job post request attaching a file with an improper extention.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                log_file.writelines(log)            
                log_file.close()
                return resp
        else:
            message = 'You are not allowed to perform this request. Please make sure that you are logged in to the service.'
            resp = jsonify({'message' : message})
            resp.status_code = 400
            today = str(dt.date.today())
            if not os.path.exists("log"):
                os.makedirs("log")
            log_file = open("./log/log-"+today+".txt", "a")
            log_time = time.localtime()
            log_time = time.strftime("%H:%M:%S", log_time)
            log = f"************************************************\n{log_time}: An unknown user tried to make a job post request to the system.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
            log_file.writelines(log)            
            log_file.close()
            return resp

    def get(self):
        
        if not request.json:
            message = 'Please make sure to send a valid request. Your request lacks a json payload.'
            resp = jsonify({'message' : message})
            resp.status_code = 400
            today = str(dt.date.today())
            if not os.path.exists("log"):
                os.makedirs("log")
            log_file = open("./log/log-"+today+".txt", "a")
            log_time = time.localtime()
            log_time = time.strftime("%H:%M:%S", log_time)
            log = f"************************************************\n{log_time}: An unknown user tried to make a job get request to the system without attaching any json payload.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
            log_file.writelines(log)            
            log_file.close()
            return resp
        entry_dict = request.json
        if not "token" in entry_dict:
            message = 'Please make sure to send a valid request. Your json payload lacks a token key'
            resp = jsonify({'message' : message})
            resp.status_code = 400
            today = str(dt.date.today())
            if not os.path.exists("log"):
                os.makedirs("log")
            log_file = open("./log/log-"+today+".txt", "a")
            log_time = time.localtime()
            log_time = time.strftime("%H:%M:%S", log_time)
            log = f"************************************************\n{log_time}: An unknown user tried to make a job get request to the system without using the authintication token.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
            log_file.writelines(log)            
            log_file.close()
            return resp 
        token = entry_dict.get("token")
        user = token_authentication(token)
        
        if user:
            if not "ticket" in entry_dict:
                message = 'Please make sure to send a valid request. Your json payload lacks a ticket key'
                resp = jsonify({'message' : message})
                resp.status_code = 400
                today = str(dt.date.today())
                if not os.path.exists("log"):
                    os.makedirs("log")
                log_file = open("./log/log-"+today+".txt", "a")
                log_time = time.localtime()
                log_time = time.strftime("%H:%M:%S", log_time)
                log = f"************************************************\n{log_time}: The user with the username: '{user}' tried to make a job get request to the system without using a ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                log_file.writelines(log)            
                log_file.close()
                return resp 
            else:
                ticket = entry_dict.get("ticket")
                result = check_status(ticket, token)
                if result == -1:
                    message = 'Please make sure to send a valid request. Your json payload has an invalid ticket'
                    resp = jsonify({'message' : message})
                    resp.status_code = 400
                    today = str(dt.date.today())
                    if not os.path.exists("log"):
                        os.makedirs("log")
                    log_file = open("./log/log-"+today+".txt", "a")
                    log_time = time.localtime()
                    log_time = time.strftime("%H:%M:%S", log_time)
                    log = f"************************************************\n{log_time}: The user with the username: '{user}' tried to make a job get request to the system using an invalid ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                    log_file.writelines(log)            
                    log_file.close()
                    return resp                
                
                if result == 0:
                    message = 'Your request is yet to be attended. Please try again in a few minutes'
                    resp = jsonify({'message' : message})
                    resp.status_code = 200
                    today = str(dt.date.today())
                    if not os.path.exists("log"):
                        os.makedirs("log")
                    log_file = open("./log/log-"+today+".txt", "a")
                    log_time = time.localtime()
                    log_time = time.strftime("%H:%M:%S", log_time)
                    log = f"************************************************\n{log_time}: The user with the username: '{user}' made a job get request to the system using an a valid ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                    log_file.writelines(log)            
                    log_file.close()
                    return resp 
                if result == -2:
                    message = 'Your request was declined. Only the file owner can see it\'s status'
                    resp = jsonify({'message' : message})
                    resp.status_code = 400
                    today = str(dt.date.today())
                    if not os.path.exists("log"):
                        os.makedirs("log")
                    log_file = open("./log/log-"+today+".txt", "a")
                    log_time = time.localtime()
                    log_time = time.strftime("%H:%M:%S", log_time)
                    log = f"************************************************\n{log_time}: The user with the username: '{user}' tried to make a job get request to a file owned by other user.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                    log_file.writelines(log)            
                    log_file.close()
                    return resp    
                else:   
                    message = 'Your request is ready. Please use your ticket to request your file from http://hostname.upm.es/api/research_object/'
                    resp = jsonify({'message' : message})
                    resp.status_code = 200
                    today = str(dt.date.today())
                    if not os.path.exists("log"):
                        os.makedirs("log")
                    log_file = open("./log/log-"+today+".txt", "a")
                    log_time = time.localtime()
                    log_time = time.strftime("%H:%M:%S", log_time)
                    log = f"************************************************\n{log_time}: The user with the username: '{user}' made a job get request to the system using an a valid ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                    log_file.writelines(log)            
                    log_file.close()
                    return resp
        else:
            message = 'You are not allowed to perform this request. Please make sure that you are logged in to the service.'
            resp = jsonify({'message' : message})
            resp.status_code = 400
            today = str(dt.date.today())
            if not os.path.exists("log"):
                os.makedirs("log")
            log_file = open("./log/log-"+today+".txt", "a")
            log_time = time.localtime()
            log_time = time.strftime("%H:%M:%S", log_time)
            log = f"************************************************\n{log_time}: An unknown user tried to make a job get request to the system.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
            log_file.writelines(log)            
            log_file.close()
            return resp

class login(Resource):
    def post(self):
        if 'username' not in request.json or 'userpassword' not in request.json:
            message = 'Please make sure to send a valid request. Your request is missing a username and/or a password'
            resp = jsonify ({'message' : message})
            resp.status_code = 401
            today = str(dt.date.today())
            if not os.path.exists("log"):
                os.makedirs("log")
            log_file = open("./log/log-"+today+".txt", "a")
            log_time = time.localtime()
            log_time = time.strftime("%H:%M:%S", log_time)
            log = f"************************************************\n{log_time}: An unknown user tried to login to the system without providing any credentials.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
            log_file.writelines(log)            
            log_file.close()
            return resp
        entry_dict = request.json
        conn = sql.connect("./Database/enrrichmentDB.db")
        cursor = conn.cursor()
        username = entry_dict.get("username")
        
        
        instruction = f"SELECT * FROM users WHERE username = '{username}'"
        result = cursor.execute (instruction)
        for user in result.fetchall():
            if check_password_hash(user[2],entry_dict.get("userpassword")):
                CURRENT_USER = user
                token = jwt.encode({'id':user[0]}, SECRET_KEY, "HS256")
                
                user = user [1]
                message = 'Logged in successfully. Please recover your token'
                resp = jsonify ({'message':message, 'token':token})
                resp.status_code = 200

                today = str(dt.date.today())
                if not os.path.exists("log"):
                    os.makedirs("log")
                log_file = open("./log/log-"+today+".txt", "a")
                log_time = time.localtime()
                log_time = time.strftime("%H:%M:%S", log_time)
                log = f"************************************************\n{log_time}: The user with the username: '{user}' logged in successfully to the system.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                log_file.writelines(log)            
                log_file.close()
                return resp
            else:
                message = 'Login request declined! Please make sure to send a valid username and password'
                resp = jsonify ({'message' : message})
                resp.status_code = 401
                today = str(dt.date.today())
                if not os.path.exists("log"):
                    os.makedirs("log")
                log_file = open("./log/log-"+today+".txt", "a")
                log_time = time.localtime()
                log_time = time.strftime("%H:%M:%S", log_time)
                log = f"************************************************\n{log_time}: An unknown user tried to login to the system providing invalid credentials.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                log_file.writelines(log)            
                log_file.close()
                return resp
            
class research_object (Resource):
    def get(self):
        token = request.json.get('token')
        user = token_authentication(token)
        if user:
            if not "token" in request.json:
                message = 'Please make sure to send a valid request. It seems like you are not logged in the system.'
                resp = jsonify({'message' : message})
                resp.status_code = 400
                today = str(dt.date.today())
                if not os.path.exists("log"):
                    os.makedirs("log")
                log_file = open("./log/log-"+today+".txt", "a")
                log_time = time.localtime()
                log_time = time.strftime("%H:%M:%S", log_time)
                log = f"************************************************\n{log_time}: An unknown user sent a download request to the system.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                log_file.writelines(log)            
                log_file.close()
                return resp
            
            token = request.json.get("token")
            if not "ticket" in request.json:
                message = 'Please make sure to send a valid request. Your json payload lacks a ticket key'
                resp = jsonify({'message' : message})
                resp.status_code = 400
                today = str(dt.date.today())
                if not os.path.exists("log"):
                    os.makedirs("log")
                log_file = open("./log/log-"+today+".txt", "a")
                log_time = time.localtime()
                log_time = time.strftime("%H:%M:%S", log_time)
                log = f"************************************************\n{log_time}: The user with the username '{user}' sent a download request without any ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                log_file.writelines(log)            
                log_file.close()
                return resp
            
            else:
                ticket = request.json.get("ticket")
                status = check_status(ticket, token)
                print(status)
                if status == -2:
                    message = 'Couldn\'t download file. Only the file owner can download the file.'
                    resp = jsonify({'message' : message})
                    resp.status_code = 400
                    today = str(dt.date.today())
                    if not os.path.exists("log"):
                        os.makedirs("log")
                    log_file = open("./log/log-"+today+".txt", "a")
                    log_time = time.localtime()
                    log_time = time.strftime("%H:%M:%S", log_time)
                    log = f"************************************************\n{log_time}: The user with the username '{user}' sent a download request for a file belonging to other user.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                    log_file.writelines(log)            
                    log_file.close()
                    return resp
                if status == -1:
                    message = 'Couldn\'t download file. The ticket you entered isn\'t valid.'
                    resp = jsonify({'message' : message})
                    resp.status_code = 400
                    today = str(dt.date.today())
                    if not os.path.exists("log"):
                        os.makedirs("log")
                    log_file = open("./log/log-"+today+".txt", "a")
                    log_time = time.localtime()
                    log_time = time.strftime("%H:%M:%S", log_time)
                    log = f"************************************************\n{log_time}: The user with the username '{user}' sent a download request with an invalid ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                    log_file.writelines(log)            
                    log_file.close()   
                    return resp
                if status == 0:
                    message = 'Couldn\' download file. Your file isn\'t ready yet.'
                    resp = jsonify({'message' : message})
                    resp.status_code = 400
                    today = str(dt.date.today())
                    if not os.path.exists("log"):
                        os.makedirs("log")
                    log_file = open("./log/log-"+today+".txt", "a")
                    log_time = time.localtime()
                    log_time = time.strftime("%H:%M:%S", log_time)
                    log = f"************************************************\n{log_time}: The user with the username '{user}' sent a download request for a file that isn't ready yet.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                    log_file.writelines(log)            
                    log_file.close() 
                    return resp
                else:
                    resp = send_file(app.config['DOWNLOAD_FOLDER'] + '/' + ticket+".jsonld", attachment_filename="enriched_"+status)
                    resp.status_code = 200
                    message = "Downloaded successfully"
                    today = str(dt.date.today())
                    if not os.path.exists("log"):
                        os.makedirs("log")
                    log_file = open("./log/log-"+today+".txt", "a")
                    log_time = time.localtime()
                    log_time = time.strftime("%H:%M:%S", log_time)
                    log = f"************************************************\n{log_time}: The user with the username '{user}' downloaded successfully the file related to the ticket '{ticket}'\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
                    log_file.writelines(log)            
                    log_file.close() 
                    return resp
        else:
            message = 'You are not allowed to perform this request. Please make sure that you are logged in to the service.'
            resp = jsonify({'message' : message})
            resp.status_code = 400
            today = str(dt.date.today())
            if not os.path.exists("log"):
                os.makedirs("log")
            log_file = open("./log/log-"+today+".txt", "a")
            log_time = time.localtime()
            log_time = time.strftime("%H:%M:%S", log_time)
            log = f"************************************************\n{log_time}: An unknown user tried to make a download request to the system.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n"
            log_file.writelines(log)            
            log_file.close()
            return resp

                
def signup(entry_dict:dict):
    entry_dict = {'username':'user2','userpassword':'password123'}
    conn = sql.connect("./Database/enrrichmentDB.db")
    cursor = conn.cursor()
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
    print ("Server is up and running")
    app.run(debug=True)
