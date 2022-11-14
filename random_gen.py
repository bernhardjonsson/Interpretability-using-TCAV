import os
import random
import shutil

source = "Data"
destination = "Random"
nr_of_random = 1
nr_of_pic = 2

for i in range(nr_of_random+1):
    folder_name = "random500_" + str(i)
    des_dir = os.path.join(destination,folder_name)
    for i in range(nr_of_pic):
        rand_folder = random.choice(os.listdir(source))
        img_path = os.path.join(source,rand_folder)
        img = random.choice(os.listdir(img_path))
        img_path = os.path.join(img_path,img)
        des_path = os.path.join(des_dir,img)
        try:
            shutil.copyfile(img_path,des_path)
            print("Copying file, " + img_path + " to " + des_path)
        except FileNotFoundError as error:
            print("Creating new directory, " + des_dir)
            os.mkdir(des_dir)
            print("Copying file, " + img_path + " to " + des_path)
            shutil.copyfile(img_path,des_path)
