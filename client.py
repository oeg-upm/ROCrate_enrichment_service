import requests, json, API_Server_v2, uuid
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3 as sql


#!curl -d 'client_id=rohub2020-frontend-devel' -d 'client_secret=194613be-6279-43ac-9b7b-b9959f28da27' -d 'username=george_hadib' -d 'password=George123#' -d 'grant_type=password' 'https://sso.apps.paas-dev.psnc.pl/auth/realms/rohub/protocol/openid-connect/token' | python -m json.tool
#!curl -d 'client_id=rohub2020-frontend-devel' -d 'client_secret=194613be-6279-43ac-9b7b-b9959f28da27' -d 'username=oso_peligroso' -d 'password=oso_peligroso' -d 'grant_type=password' 'https://sso.apps.paas-dev.psnc.pl/auth/realms/rohub/protocol/openid-connect/token' | python -m json.tool

#resp = requests.post('http://localhost:8008', data=data)

#print (resp)


def signup(entry_dict:dict):
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
   
    return 1
  
entry_dict = {'username':'NEW_USERNAME','userpassword':'NEW_PASSWORD'}

  
if __name__ == "__main__":
  
  signup(entry_dict)
  

  
  
  
