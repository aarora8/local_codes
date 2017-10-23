import os
import sys
import numpy as np
from scipy import misc
import matplotlib.pyplot as plt

def write_kaldi_matrix(file_handle, matrix, key):
    file_handle.write(key + " [ ")
    num_rows = len(matrix)
    if num_rows == 0:
        raise Exception("Matrix is empty")
    num_cols = len(matrix[0])

    for row_index in range(len(matrix)):
        if num_cols != len(matrix[row_index]):
            raise Exception("All the rows of a matrix are expected to "
                            "have the same length")
        file_handle.write(" ".join(map(lambda x: str(x), matrix[row_index])))
        if row_index != num_rows - 1:
            file_handle.write("\n")
    file_handle.write(" ]\n")

def get_scaled_image(im):
    scale_size = 40
    sx = im.shape[1]
    sy = im.shape[0]
    scale = (1.0 * scale_size) / sy
    nx = int(scale_size)
    ny = int(scale * sx)
    im = misc.imresize(im, (nx, ny))

    padding_x = max(1,int(0.05*im.shape[1]))
    padding_y = im.shape[0]
    im_pad = np.concatenate((255 * np.ones((padding_y,padding_x), dtype=int), im), axis=1)
    im_pad1 = np.concatenate((im_pad,255 * np.ones((padding_y, padding_x), dtype=int)), axis=1)
    return im_pad1

image_path = os.path.join('/Users/ashisharora/Desktop/summer/hcr data/lines/a01','check.png')
im = misc.imread(image_path)
im_scale = get_scaled_image(im)

data = np.transpose(im_scale, (1, 0))
data = np.divide(data, 255.0)
write_kaldi_matrix(sys.stdout, data, '1')