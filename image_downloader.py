import random
from urllib import request
import os

def image_downloader(link_to_image, user_dir):
    image_name = random.randrange(1, 1000)
    failure = 0  #  Checking failure status
    try:
        os.chdir(user_dir)
    except OSError:
        user_choice = input("Directory does not exists. Press Y to create new directory...")
        if user_choice == 'Y' or user_choice == 'y':
            print("Creating directory... \n Downloading file...")
            os.mkdir(user_dir)
            os.chdir(user_dir)
        else:
            print("File Downloading Failed!!!")
            failure = 1
    finally:
        if failure == 1:
            return
        else:
            full_name = str(image_name) + '.jpg'
            request.urlretrieve(link_to_image, full_name)
            return

user_input_link = input("Please enter your Link : ")
# no need for this line -> user_input_link = user_input_link[1: -1]
print(user_input_link)

directory_to_save = input("Please enter path: ")

# print(os.getcwd())
# os.mkdir(directory_to_save)

image_downloader(user_input_link, directory_to_save)