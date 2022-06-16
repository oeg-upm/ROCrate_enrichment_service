import shutil
import glob

import os
paths = ["./pending_jobs/","./done_jobs/"]

def delete_jobs():
    for path in paths:
        for file_name in os.listdir(path):
            # construct full file path
            file = path + file_name
            if os.path.isfile(file):
                print('Deleting file:', file)
                os.remove(file)
        
delete_jobs()