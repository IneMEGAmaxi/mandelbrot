#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.path.insert(0,'.')

import CPPmandelbrot_set 
from mandelbrot_set import Mandelbrot
from visualisation import show_image
import numpy as np

if __name__ == '__main__':
    m=Mandelbrot(100,1000)
    c = m.c_val
    img = np.ndarray(c.shape, dtype=np.float64)
    CPPmandelbrot_set.mandelbrot(c, m.N, img)
    show_image(img, m.N)

#M3 pro
#L1
#5 P cores: 192 KiB per core = 1 572 864 bits = 24 576 float64 --> (complex + float) = 8.192 values of array 
#6 E cores: 128 KiB per core

#L2
# P cores: 16 MiB = shared between 5 cores
# E cores: 4 MiB =  shared between 6 cores

#SLC (system level cache) = 12 MiB