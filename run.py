import threading, enrichment, API_Server_v2
from crontab import CronTab






def run_deletion():
        cron = CronTab(user="root")
        task = cron.new(command='py deletion.py') 
        task.day.every(2)
        cron.write()
       
        
def run_enrichment():
        enrichment.enrich_RO()  
        print("enrichment.py is up and running")
 
            
def run_server():
        API_Server_v2.app.run()
        print("API_Server_v2.py is up and running")
        
        


t1= threading.Thread(target=run_server)
t2= threading.Thread(target=run_enrichment)
t3= threading.Thread(target=run_deletion)
t2.setDaemon(True)
t3.setDaemon(True)
t1.start()
t2.start()
t3.start()