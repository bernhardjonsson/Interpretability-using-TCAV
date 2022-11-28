import imageio as iio
import array as arr
import os
import numpy as np


def find_color(img):
    col_count = []
    for i in range(1,12):
        col_count.append(list(img.flatten()).count(i))
    
    return np.argmax(np.array(col_count)) + 1

def rename_img(source_dir):
    dir = os.path.join(source_dir,'broden1_224','broden1_224','images')
    colors = {1: 'black-c',2:'grey-c',3:'white-c',4:'brown-c',5:'green-c',6:'pink-c',7:'purple-c',8:'blue-c',9:'yellow-c',10:'red-c',11:'orange-c'}

    for dir_name in os.listdir(dir):
        if not dir_name.startswith("."):
            for filename in os.listdir(os.path.join(dir,dir_name)):
                f = os.path.join(dir,dir_name,filename)
                if os.path.isfile(f) and "color" in filename:
                    img = iio.imread(f)
                    col = find_color(img)
                    if not filename.startswith(colors[col]):
                        new_name = colors[col] + '_' + filename
                        os.rename(f,os.path.join(dir,dir_name,new_name))