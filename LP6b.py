# 6)B) Write a python program to create a ZIP file of a particular folder which contains several files inside it.

import zipfile 
import os
def create_zip_folder(folder_path, zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zip_file: 
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file) 
                zip_file.write(file_path, file)
    print(f'{zip_file_path} created successfully!')

folder_path = input("Enter the folder path : ")
zip_file_path = input("Enter the zip file path : ")
create_zip_folder(folder_path, zip_file_path)
