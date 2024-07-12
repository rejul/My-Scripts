import os
import sys
import re

from shutil import move
directory_path=os.path.dirname(os.path.abspath(sys.argv[0]))
def sort_files(directory_path):
    for filename in os.listdir(directory_path):
        resume_exist=re.findall(r'resume.*\.(pdf|docx)$', filename, re.IGNORECASE)
        #print(f"{resume_exist},{filename}")
        if resume_exist:
         #Sprint("me")



         if os.path.isfile(os.path.join(directory_path, filename)):

            #file_extension = './resume'
            
            destination_directory = os.path.join(directory_path, 'resume')
            move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))
         if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)
            move(os.path.join(directory_path, filename), os.path.join(destination_directory, filename))



sort_files(directory_path)