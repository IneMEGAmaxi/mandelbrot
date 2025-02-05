# -*- coding: utf-8 -*-

"""Tests for mandelbrot package."""

import sys
sys.path.insert(0,'.')

from random import random
import numpy as np
import mandelbrot.mandelbrot_set as mb

def test_mandelbrot_set():
    # any complex nr norm>2 should return 0
    for i in range(10):
        n = random()*2
        m = np.sqrt(4-n**2)
        eps = 1E-9
        c = n + eps + (m+eps)*1j
        value = mb.mandelbrot_set(c)
        exp_value = 0
        assert value == exp_value
    # 0 +0j should return -1 (or <0)
    assert mb.mandelbrot_set(0+0j)<0
    
def test_mandelbrot_img():
    img = mb.mandelbrot_img()
    from matplotlib import pyplot as plt
    plt.imshow(img)
    plt.show()

# ==============================================================================
# The code below is for debugging a particular test in eclipse/pydev.
# (otherwise all tests are normally run with pytest)
# Make sure that you run this code with the project directory as CWD, and
# that the source directory is on the path
# ==============================================================================
if __name__ == "__main__":
    the_test_you_want_to_debug = test_mandelbrot_set

    print("__main__ running", the_test_you_want_to_debug)
    the_test_you_want_to_debug()
    print('-*# finished #*-')

# eof