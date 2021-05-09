import os
import shutil
import time 

def main():
    deleted_folderscount = 0
    deleted_filescount = 0 
    path = "/pathtodelete"
    days = 30
    seconds = time.time()-(days*24*60*60)

    if os.path.exists(path):
        for root_folder, folders, files in os.walk(path):
            if seconds >= get_file_or_folder_age(root_folder):
                remove_folder(root_folder)
                deleted_folderscount += 1
                break
            
            else:
                for folder in folders :
                    folder_path = os.path.join(root_folder, folder)

                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folderscount += 1
                

                for file in files : 
                    file_path = os.path.join(root_folder, file)

                    if seconds >= get_file_or_folder_age(file_path):
                        remove_file(file_path)
                        deleted_filescount +=1 
    
    else:
        print("Path is not found")
        deleted_folderscount += 1
    
    print("Total folders deleted:{deleted_folderscount}")
    print("Total files deleted:{deleted_filescount}")

def remove_folder(path):
    if not shutil.rmtree(path):
        print("Path is removed successfully")
    else:
        print("Path is not removed successfully")
    
def remove_file(path):
    if not os.remove(path):
        print("Path is removed successfully")
    else:
        print("Path is not removed successfully")

def get_file_or_folder_age(path):
    ctime = os.stat(path).st_ctime
    return ctime
 
if __name__ == '__main__':
    main()