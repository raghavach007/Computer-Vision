import numpy as np
from Affine import *

K = 3
threshold = 1
ITER_NUM = 2000

def residual_lengths(X, Y, s, t):
    e = np.dot(X, s) + Y
    diff_square = np.power(e - t, 2)
    residual = np.sqrt(np.sum(diff_square, axis=0))
    return residual

def ransac_fit(pts_s, pts_t):
    # Your ransac_fit code goes here
    pass