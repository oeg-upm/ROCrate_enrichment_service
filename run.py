import os, sys, threading, time, enrichment, API_Server_v2, deletion
import subprocess
from apscheduler.schedulers.background import BackgroundScheduler
from crontab import CronTab  






def run_deletion():
        cron = CronTab(user='Geo') 
        task = cron.new(command='py deletion.py') 
        task.day.every(2)
        cron.write()
        '''
        scheduler = BackgroundScheduler()
        scheduler.add_job(deletion.delete_jobs, 'interval', hours=48)
        scheduler.start()
        '''
        
def run_enrichment():
        enrichment.enrich_RO()  
        print("enrichment.py is up and running")
 
            
def run_server():
        API_Server_v2.app.run()
        print("API_Server_v2.py is up and running")
        
        
'''
subprocess.run("python enrichment.py &", shell=True)
print("HERE")

process1 = subprocess.Popen(r'.\\enrichment.py &',shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

my_pid, err = process1.communicate()

if len(my_pid.splitlines()) >0:
        sys.exit(0);


process2 = subprocess.Popen(r'.\\API_Server_v2.py',shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)

my_pid, err = process2.communicate()

if len(my_pid.splitlines()) >0:
        sys.exit(0);
        
'''

t1= threading.Thread(target=run_server)
t2= threading.Thread(target=run_enrichment)
t3= threading.Thread(target=run_deletion)
t2.setDaemon(True)
t3.setDaemon(True)
t1.start()
t2.start()
t3.start()