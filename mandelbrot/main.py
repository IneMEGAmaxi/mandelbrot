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
