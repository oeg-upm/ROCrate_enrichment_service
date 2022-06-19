import threading, enrichment, API_Server_v2
from crontab import CronTab
import sqlite3 as sql






def run_deletion():
        cron = CronTab(user="root")
        task = cron.new(command='py deletion.py') 
        task.day.every(2)
        cron.write()
       
        
def run_enrichment():
        enrichment.enrich_RO()  
        print("enrichment.py is up and running")
 
            
def run_server():
        API_Server_v2.app.run(debug=True,host="0.0.0.0",port=5000)
        print("API_Server_v2.py is up and running")
        
        
def create_database():
    conn = sql.connect("./Database/enrrichmentDB.db")
    cursor = conn.cursor()                
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id text NOT NULL UNIQUE PRIMARY KEY,
    username text NOT NULL, 
    userpassword text NOT NULL,
    admin boolean DEFAULT 0)""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS jobs (
    job_id text NOT NULL, 
    original_name text NOT NULL, 
    client text NOT NULL, 
    ready boolean NOT NULL)""")
    conn.close()
    return
    

    
    


create_database()
t1= threading.Thread(target=run_enrichment)
t2= threading.Thread(target=run_deletion)
t1.setDaemon(True)
t2.setDaemon(True)
t1.start()
t2.start()
run_server()