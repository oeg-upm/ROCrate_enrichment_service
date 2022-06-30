from flask import Flask, request, jsonify, send_file
from flask_restful import Api, Resource
import os, uuid, jwt, json, time, datetime as dt, sqlite3 as sql, logging,logging
from waitress import serve
import re

from werkzeug.security import  check_password_hash, generate_password_hash
from logging import Formatter
from logging.handlers import TimedRotatingFileHandler
from functools import wraps





UPLOAD_FOLDER = './pending_jobs'
DOWNLOAD_FOLDER = './done_jobs'
SECRET_KEY = 'MY_PASSWORD'
LOGGING_FOLDER = './log'
ALLOWED_EXTENSIONS = {'json', 'jsonld'}

# Start the flask API app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config["LOGGING_FOLDER"] = LOGGING_FOLDER
app.config['SECRET_KEY'] = SECRET_KEY
app.config['CURRENT_USER'] = None
api = Api(app)  


def config_logger():
    logname = app.config["LOGGING_FOLDER"] + "/API.log"
    app.logger.setLevel(logging.DEBUG)   
    
    formatter = Formatter('%(asctime)s %(levelname)s: %(message)s',datefmt="%m/%d/%Y %I:%M:%S %p %Z")
    handler = TimedRotatingFileHandler(filename = logname, when="midnight", interval=1)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    handler.suffix = "%d%m%Y"
    handler.extMatch = re.compile(r"^\d{8}$") 
    app.logger.handlers.clear()
    app.logger.addHandler(handler) 
    #app.logger.debug("debuggggggggggggg")
    
    


'''def log_file ():
    today = str(dt.date.today())            
    log_file = open("./log/log-"+today+".txt", "a")
    return log_file'''

def allowed_file(filename):
    	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
 
'''def token_authentication (token):
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
        return result[0]

    return False
'''
def token_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):

        token = None

        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            
            resp = jsonify({'message': 'a valid token is missing'})
            resp.status_code = 401
            return resp
        try:

            data = jwt.decode(token, app.config['SECRET_KEY'], "HS256")
            try:
                id = data.get("id")
            except:
                resp = jsonify({'message': 'token is invalid'})
                resp.status_code = 401
                return resp
            conn = sql.connect("./Database/enrrichmentDB.db")
            cursor = conn.cursor()
        
            instruction = f"SELECT * FROM users WHERE id = '{id}'"
            result = cursor.execute(instruction).fetchone()
            if (result):
                app.config["CURRENT_USER"] = result
                
            else:
                resp = jsonify({'message': 'token is invalid'})
                resp.status_code = 401
                return resp
        except:
            resp = jsonify({'message': 'token is invalid'})
            resp.status_code = 401
            return resp
        
        return f(result, *args, **kwargs)
    return decorator


def check_status (ticket: str, user_id: str):
    conn = sql.connect("./Database/enrrichmentDB.db")
    cursor = conn.cursor()
    instruction = f"SELECT * FROM jobs WHERE job_id = '{ticket}'"
    
    result = cursor.execute(instruction).fetchone()

    
    if not result:
        return (-1)
    else:
        if result[2] == user_id:
            ready = result[3]
            if ready > 0:
                return result[1]    
            return 0  
        else:
            return -2
    
   

class Jobs (Resource):
    
    @token_required
    def post(self, result):
        user_id = app.config["CURRENT_USER"][0]
        username = app.config["CURRENT_USER"][1]        
        if 'file' not in request.files:

            message = 'No file part in the request. Please make sure to upload the json/jsonld file.'
            resp = jsonify({'message' : message})
            resp.status_code = 400
            
            #ATENCION AQUI CON EL LOG
            
            if not os.path.exists("log"):
                os.makedirs("log")
            
            
            
            
            app.logger.info (msg=f"The user with the username: '{username}' made a jobs Post request without attaching any file.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************")
            
            
            #########################################################
            
            return resp
            
        file = request.files['file']
        print("AQUI")
        if file.filename == '':
            print("AQUI")

            message = 'No file selected for uploading. Please make sure to upload the json/jsonld file.'
            
            resp = jsonify({'message' : message})
            resp.status_code = 400
            
            #ATENCION AQUI CON EL LOG
            if not os.path.exists("log"):
                os.makedirs("log")
            
            app.logger.info (msg=f"The user with the username: '{username}' made a jobs Post request without attaching any file.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 
          
            ##########################################################
            
            
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
            user_id = app.config["CURRENT_USER"][0]
                      
            instruction = f"INSERT INTO jobs VALUES ('{ticket}','{file.filename}','{user_id}',FALSE)"
            cursor.execute(instruction)
            conn.commit()
            conn.close
            message = 'File successfully uploaded. Please recover your ticket: '+ ticket
            resp = jsonify({'message' : message, 'ticket' : ticket})
            resp.status_code = 201
            
            #ATENCION AQUI CON EL LOG
            
            
            if not os.path.exists("log"):
                os.makedirs("log")
                
            app.logger.info (msg=f"The user with the username: '{username}' made a successful jobs Post request.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

            
            ################################################
            return resp

        else:
            message = 'Please make sure to upload a valid file type. Allowed file types are json and jsonld'
            resp = jsonify({'message' : message})
            resp.status_code = 400
            
            #ATENCION AQUI CON EL LOG
            username = app.config["CURRENT_USER"][1]
            if not os.path.exists("log"):
                os.makedirs("log")
                        
            app.logger.info (msg=f"The user with the username: '{username}' made a jobs post request attaching a file with an improper extention.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

            ####################################################
            
            return resp
    
        
    @token_required
    def get(self,result):
        user_id = app.config["CURRENT_USER"][0]
        username = app.config["CURRENT_USER"][1]
        conn = sql.connect("./Database/enrrichmentDB.db")
        cursor = conn.cursor()
        instruction = f"SELECT * FROM jobs WHERE client = '{user_id}'"
        result = cursor.execute(instruction).fetchall()
        resp = jsonify({"jobs":result})
        resp.status_code = 200
        app.logger.info (msg=f"The user with the username: '{username}' made a jobs Get request.\nStatus_code: '{resp.status_code}'\n**********************************************") 

        
        return resp
    

        
    
    
class Job (Resource):    
    @token_required
    def get(self,  result, ticket):
        user_id = app.config["CURRENT_USER"][0]
        username = app.config["CURRENT_USER"][1]
        if not ticket:
            #AQUI HAY QUE PRESTAR ATENCION
        
            message = 'Please make sure to send a valid request. Your request lacks a valid ticket.'
            resp = jsonify({'message' : message})
            resp.status_code = 400
            
            # AQUI ATENCION CON EL LOG
            if not os.path.exists("log"):
                os.makedirs("log")
            
            app.logger.info (msg=f"The user with the username: '{username}' tried to make a job get request to the system without using any ticker.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

            ######################################################
            
            return resp
        '''entry_dict = request.json
        if not "token" in entry_dict:
            message = 'Please make sure to send a valid request. Your json payload lacks a token key'
            resp = jsonify({'message' : message})
            resp.status_code = 401
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
            else:'''
        

        result = check_status(ticket, user_id)
        if result == -1:
            message = 'Please make sure to send a valid request. Your json payload has an invalid ticket'
            resp = jsonify({'message' : message})
            resp.status_code = 404
            if not os.path.exists("log"):
                os.makedirs("log")
            
            app.logger.info (msg=f"The user with the username: '{username}' tried to make a job get request to the system using an invalid ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

            
            return resp                
                
        if result == 0:
            message = 'Your request is yet to be attended. Please try again in a few minutes'
            resp = jsonify({'message' : message})
            resp.status_code = 200
            if not os.path.exists("log"):
                os.makedirs("log")
           
            
            app.logger.info (msg=f"The user with the username: '{username}' made a successful job get request to the system using a valid ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

            return resp 
        if result == -2:
            message = 'Your request was declined. Only the file owner can see it\'s status'
            resp = jsonify({'message' : message})
            resp.status_code = 401

            if not os.path.exists("log"):
                os.makedirs("log")
           
            app.logger.info (msg=f"The user with the username: '{username}' tried to make a job get request to a file owned by other user.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

            return resp    
        else:   
            message = f"Your request is ready. Please use your ticket to request your file from https://ro-enrichment.linkeddata.es/api/research_object/{ticket}/"
            link = f"https://ro-enrichment.linkeddata.es/api/research_object/{ticket}/"
            resp = jsonify({'message' : message, "link":link})
            resp.status_code = 200
            
            if not os.path.exists("log"):
                os.makedirs("log")
   
            app.logger.info (msg=f"The user with the username: '{username}' made a successful job get request to the system using a valid ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

            
            return resp
        '''else:
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
'''
class login(Resource):
    
    def post(self):
        if 'username' not in request.json or 'userpassword' not in request.json:
            message = 'Please make sure to send a valid request. Your request is missing a username and/or a password'
            resp = jsonify ({'message' : message})
            resp.status_code = 401

            if not os.path.exists("log"):
                os.makedirs("log")
     
            app.logger.info (msg=f"An unknown user tried to login to the system without providing any credentials.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

            return resp
        entry_dict = request.json
        conn = sql.connect("./Database/enrrichmentDB.db")
        cursor = conn.cursor()
        username = entry_dict.get("username")
        
        
        instruction = f"SELECT * FROM users WHERE username = '{username}'"
        result = cursor.execute (instruction)
        for user in result.fetchall():
            if check_password_hash(user[2],entry_dict.get("userpassword")):
                token = jwt.encode({'id':user[0]}, SECRET_KEY, "HS256")
                
                user = user [1]
                message = 'Logged in successfully. Please recover your token'
                resp = jsonify ({'message':message, 'token':token})
                resp.status_code = 200

                if not os.path.exists("log"):
                    os.makedirs("log")
             
                app.logger.info (msg=f"The user with the username: '{user}' logged in successfully to the system.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

     
                return resp
            else:
                message = 'Login request declined! Please make sure to send a valid username and password'
                resp = jsonify ({'message' : message})
                resp.status_code = 401
                if not os.path.exists("log"):
                    os.makedirs("log")
                
                app.logger.info (msg=f"An unknown user tried to login to the system providing invalid credentials.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

                return resp
            
class research_object (Resource):
    
    @token_required
    def get(self, result, ticket):
        
        #######################################################################
        user_id = app.config["CURRENT_USER"][0]
        username = app.config["CURRENT_USER"][1]
        #######################################################################
    
        if not ticket:
            message = 'Please make sure to send a valid request. Your json payload lacks a ticket key'
            resp = jsonify({'message' : message})
            resp.status_code = 400

            if not os.path.exists("log"):
                os.makedirs("log")
            
            app.logger.info (msg=f"The user with the username '{username}' sent a download request without any ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

            
            return resp
       
        else:
           
            status = check_status(ticket, user_id)
            if status == -2:
                message = 'Couldn\'t download file. Only the file owner can download the file.'
                resp = jsonify({'message' : message})
                resp.status_code = 400

                if not os.path.exists("log"):
                    os.makedirs("log")
               
                app.logger.info (msg=f"The user with the username '{username}' sent a download request for a file belonging to other user.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

                return resp
            if status == -1:
                message = 'Couldn\'t download file. The ticket you entered isn\'t valid.'
                resp = jsonify({'message' : message})
                resp.status_code = 400

                if not os.path.exists("log"):
                    os.makedirs("log")
        
                app.logger.info (msg=f"The user with the username '{username}' sent a download request with an invalid ticket.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

       
                return resp
            if status == 0:
                message = 'Couldn\' download file. Your file isn\'t ready yet.'
                resp = jsonify({'message' : message})
                resp.status_code = 400

                if not os.path.exists("log"):
                    os.makedirs("log")
          
                app.logger.info (msg=f"The user with the username '{username}' sent a download request for a file that isn't ready yet.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

              
                return resp
            else:
                resp = send_file(app.config['DOWNLOAD_FOLDER'] + '/' + ticket+".jsonld", attachment_filename="enriched_"+status)
                resp.status_code = 200
                message = "Downloaded successfully"
                
                if not os.path.exists("log"):
                    os.makedirs("log")
                
                app.logger.info (msg=f"The user with the username '{username}' downloaded successfully the file related to the ticket '{ticket}'.\nStatus_code: '{resp.status_code}'\nMessage: '{message}'\n**********************************************") 

                return resp
                

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
api.add_resource(Job, "/api/job/<string:ticket>/")
api.add_resource(login,"/api/login/")
api.add_resource(research_object, "/api/research_object/<string:ticket>/")

# Execution


if __name__ == "__main__":
    #app.run(debug=True)
    config_logger()
    serve(app,host="0.0.0.0",port=5000)
