#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Tests for C++ module mandelbrot.CPPmandelbrot_set.
"""

import sys
sys.path.insert(0,'.')

import numpy as np
from  line_profiler import profile
import mandelbrot.CPPmandelbrot_set as CPPmandelbrot_set
from mandelbrot.mandelbrot_set import Mandelbrot
from mandelbrot.visualisation import show_image
def test_cpp_mandelbrot_compare():
    m = Mandelbrot(100,1000)
    c = m.c_val
    N = m.N
    img = np.ndarray(c.shape, dtype=np.float64)
    expected_img = m.mandelbrot_img()
    CPPmandelbrot_set.mandelbrot(c,N,img)
    assert np.allclose(img, expected_img)

@profile
def test_cpp_mandelbrot():
    m = Mandelbrot(100,1000)
    c = m.c_val
    N = m.N
    img = np.ndarray(c.shape, dtype=np.float64)
    CPPmandelbrot_set.mandelbrot(c,N,img)
    show_image(img, N)



#===============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (normally all tests are run with pytest)
#===============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_cpp_mandelbrot

    print(f"__main__ running {the_test_you_want_to_debug} ...")
    the_test_you_want_to_debug()
    print('-*# finished #*-')
#===============================================================================
