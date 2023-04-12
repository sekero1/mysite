import os
import datetime
import argparse
import time

def get_img(cut_num=1):
    """ generate images, save them, and return their full filenames """

    default='/home/jae/myprj/camera/stl_img'
    folder = '{}/{}/'.format(default ,datetime.datetime.now().strftime("%y%m%d"))
    os.makedirs(folder, exist_ok=True)
    img_files =  ''  # saved  image file names which is a list

    while cut_num:
        filename = folder + datetime.datetime.now().strftime("%y%m%d_%H%M%S") + '.jpg'
        os.system('libcamera-jpeg -o {} -n'.format(filename))
        cut_num = cut_num - 1
        img_files = img_files + ',' + filename


    return img_files

