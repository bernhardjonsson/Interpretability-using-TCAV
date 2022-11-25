import os
import random
import shutil

source = r"C:\Users\Aragorn\Downloads\imagenet-object-localization-challenge.zip"
destination = "Random"
nr_of_random = 500
nr_of_pic = 200

from zipfile import ZipFile

img_count = 0
nr_of_img = nr_of_pic*(nr_of_random+1)
used_idx = []

with ZipFile(source, 'r') as zipObject:
   filename = zipObject.namelist()
   while img_count <= nr_of_img:
       img_idx = random.randint(0,len(filename))
       if "Data/CLS-LOC/train" in filename[img_idx] and img_idx  not in used_idx:
           zipObject.extract(filename[img_idx], 'tmp')
           img_count +=1
           used_idx.append(img_idx)

print(img_count)
copy_path=[]
for root,dirs,files in os.walk("tmp"):
    for file in files:
        copy_path.append(os.path.join(root,file))
random.shuffle(copy_path)
print(copy_path[0:10])
print(len(copy_path))
img_idx = 0
for i in range(nr_of_random+1):
    folder_name = "random500_" + str(i)
    des_dir = os.path.join(destination,folder_name)
    for i in range(nr_of_pic):
        img_idx += 1
        img_path = copy_path[img_idx]
        img = str(img_idx) + ".jpeg"
        des_path = os.path.join(des_dir,img)
        try:
            shutil.copyfile(img_path,des_path)
        except FileNotFoundError as error:
            print("Creating new directory, " + des_dir)
            os.mkdir(des_dir)
            shutil.copyfile(img_path,des_path)

shutil.rmtree('tmp')
