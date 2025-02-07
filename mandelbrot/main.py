#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
sys.path.insert(0,'.')

import CPPmandelbrot_set 
from mandelbrot_set import Mandelbrot
from visualisation import show_image
import numpy as np

if __name__ == '__main__': #22 threads, 180.0s
    m=Mandelbrot(10000,5000)
    c = m.c_val
    img = np.ndarray(c.shape, dtype=np.float64)
    start = time.time()
    CPPmandelbrot_set.mandelbrot(c, m.N, img)
    end = time.time()
    elapsed_time = end - start
    print(f"Execution time: {elapsed_time:.6f} seconds")
    
    show_image(img, m.N)

#M3 pro
#L1
#5 P cores: 192 KiB per core = 1 572 864 bits = 24 576 float64 --> (complex + float) = 8.192 values of array 
#6 E cores: 128 KiB per core

#L2
# P cores: 16 MiB = shared between 5 cores
# E cores: 4 MiB =  shared between 6 cores

#SLC (system level cache) = 12 MiB