This file documents a python module built from C++ code with pybind11.
You should document the Python interfaces, *NOT* the C++ interfaces.

Module mandelbrot.CPPmandelbrot_set
**************************

Module :py:mod:`CPPmandelbrot_set` built from C++ code in mandelbrot.CPPmandelbrot_set
cpp`.

.. function:: mandelbrot(c,N,img)
   :module: mandelbrot.CPPmandelbrot_set
   
   Compute the image depicting the escape iterations of 2darray the N-mandelbrot set of 2darray c.

   :param c: 2D Numpy array with ``dtype=numpy.complex128`` (input)
   :param N: int (input)
   :param img: 2D Numpy array with ``dtype=numpy.float64`` (output)
   