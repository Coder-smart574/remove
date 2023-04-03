import os
import time
import shutil

def main():
    deleted_files=0
    deleted_folders=0
    days=30
    path= r""
    seconds=time.time()-(days*86400)

    if os.path.exists(path):
        for rootfolder,folders,files in os.walk(path):
            if seconds >= get_file_or_folder_age(rootfolder):
                remove_folder(rootfolder)
                deleted_folders+=1
                break
            else:
                for folder in folders:
                    folder_path=os.path.join(rootfolder,folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folders+=1
                for file in files:
                    file_path=os.path.join(rootfolder,file)
                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_files+=1
        else:
            if seconds >= get_file_or_folder_age(path):
                remove_file(path)
                deleted_files+=1
    else:
        print("Path not Found")

def remove_folder(path):
    if not shutil.rmtree(path):
        print("Path removed")
    else:
        print("Path not removed")

def remove_file(path):
    if not os.remove(path):
        print("Path removed")
    else:
        print("Path not removed")

def get_file_or_folder_age(path):
    return os.stat(path).st_ctime

if __name__ =="__main__":
    main()