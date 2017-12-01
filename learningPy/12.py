#!/usr/bin/env python

import argparse
import os
import sys
import scipy.io as sio
import numpy as np
from scipy import misc

from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL)

import matplotlib.pyplot as plt

### main ###
phone_width_path = os.path.join('/Users/ashisharora/Desktop',
                            'alignment.txt')

images_file_path = '/Users/ashisharora/Desktop/semesters/summer 2018/HWR/hcr data/lines'

def get_scaled_image(im):
    scale_size = 40
    sx = im.shape[1]
    sy = im.shape[0]
    scale = (1.0 * scale_size) / sy
    nx = int(scale_size)
    ny = int(scale * sx)
    im = misc.imresize(im, (nx, ny))
    padding_x = max(5,int((5/100)*im.shape[1]))
    padding_y = im.shape[0]
    im_pad = np.concatenate((255 * np.ones((padding_y,padding_x), dtype=int), im), axis=1)
    im_pad1 = np.concatenate((im_pad,255 * np.ones((padding_y, padding_x), dtype=int)), axis=1)
    return im_pad1

def get_width_vect(line):
    line_vect = line.strip().split(' ')[1:]
    line_vect_1 = " ".join(line_vect)
    line_vect_1 = line_vect_1.split(';')
    width_vect = list()
    distance_vect = list()
    distance_vect.append(0)
    for element in line_vect_1:
        element = element.strip()
        element_1 = element.split(" ")[1]
        curr_val = int(element_1)
        curr_val = curr_val * 4
        width_vect.append(curr_val)

    for curr_val in width_vect:
        previous_val = distance_vect[-1]
        new_val = previous_val + curr_val
        distance_vect.append(new_val)
    distance_vect[-1] = distance_vect[-1] - 4
    return distance_vect

with open(phone_width_path, 'rt') as pw_fh:
  for line in pw_fh:
    dist_vect = get_width_vect(line)
    line_vect = line.strip().split('_')
    folder_1 = line_vect[1].split('-')[0]
    folder_2 = line_vect[1].split(' ')[0][:-3]
    image = line_vect[1].split(' ')[0]
    folder_path = os.path.join(images_file_path, folder_1,
                                    folder_2)
    image_path = folder_path + '/' + image + '.png'
    print image_path
    im = misc.imread(image_path)
    im_scale = get_scaled_image(im)
    im_scaleNew = im_scale
    im_scaleNew[:, dist_vect] = 0
    plt.imshow(im_scaleNew)
    plt.show()

