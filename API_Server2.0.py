from urllib import response
from flask import Flask, request, Response, jsonify, send_file
from flask_restful import Api, Resource
from werkzeug.utils import secure_filename
import os, uuid
from enrichment import enrich_RO, check_return



UPLOAD_FOLDER = '/pending_jobs'
DOWNLOAD_FOLDER = '/done_jobs'
ALLOWED_EXTENSIONS = {'json', 'jsonld'}


# Start the flask API app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
api = Api(app)

def allowed_file(filename):
    	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Jobs (Resource):
    def post(self):
        if 'file' not in request.files:
            response = jsonify({'message' : 'No file part in the request. Please make sure to upload the json/jsonld file.'})
            response.status_code = 400
            return response
        
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
            
            enrich_RO(filename)
            resp = jsonify({'message' : 'File successfully uploaded',
                            'ticket' : ticket})
            resp.status_code = 201
            return resp

        else:
            resp = jsonify({'message' : 'Please make sure to upload a valid file type. Allowed file types are json and jsonld'})
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
            result = check_return(ticket)
            if result == -1:
                resp = jsonify({'message' : 'Please make sure to send a valid request. Your json payload has an invalid ticket'})
                resp.status_code = 400
                return resp   
            if result == 0:
                resp = jsonify({'message' : 'Your request is yet to be attended. Please try again in a few minutes'})
                resp.status_code = 200
                return resp
            else:   
                response = send_file(app.config['DOWNLOAD_FOLDER'] + '/' + ticket+".jsonld", attachment_filename="lksjdlad")
                response.status_code = 200
                return response


api.add_resource(Jobs,"/api/jobs/")


# Execution

if __name__ == "__main__":
    app.run(debug=True)



