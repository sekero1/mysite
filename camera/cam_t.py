import os
import datetime
import argparse
import time

parser = argparse.ArgumentParser(
    description='Long exposure with libcamera')
parser.add_argument('--o', type=str, help='output folder', default='/home/jae/myprj/camera/stl_img')
parser.add_argument('--t', type=int, default=30,
                    help='exposition time')
parser.add_argument('--g', type=int, default=5,
                    help='gain')

args = parser.parse_args()

folder = '{}/{}/'.format(args.o,datetime.datetime.now().strftime("%y%m%d"))
os.makedirs(folder, exist_ok=True)
print('Saving to {}'.format(folder))
cut_num = 5

while cut_num:
    filename = folder + datetime.datetime.now().strftime("%y%m%d_%H%M%S") + '.jpg'
    os.system(
		'libcamera-jpeg -o {}'.format(filename))
    cut_num = cut_num - 1

