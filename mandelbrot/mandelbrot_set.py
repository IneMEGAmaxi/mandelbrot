import numpy as np
from math import log
from line_profiler import profile
import numba
class Mandelbrot:#d=5000
    xmin = -2; xmax = 1; ymin = 0; ymax = 4/3
    def __init__(self, max_iter, pixel_density):
        self.N = max_iter
        self.d = pixel_density
        self.c_val = self.get_c_val()
    
    def get_c_val(self):
        x = np.linspace(self.xmin, self.xmax, int((self.xmax-self.xmin)*self.d))
        y = np.linspace(self.ymin, self.ymax, int((self.ymax-self.ymin)*self.d))
        X, Y = np.meshgrid(x,y)
        return X + Y*1j #1.49011612 GiB

    def mandelbrot_img(self):
        return get_escape_iter(self.c_val, self.N)

@numba.jit
def get_escape_iter(c_val, N):
    img = np.zeros(c_val.shape, dtype=np.float64) # 762.939453 MiB -> cache = 12 MiB 
    for (i, j), c in np.ndenumerate(c_val):
        img[i,j] = escape_iter(c, N)
    return img

#@profile
@numba.jit
def escape_iter(c, N):
    z = 0
    for i in range(N):
        z = z*z + c
        if abs(z) > 2:
            return i + 1 - log(log(abs(z))) / 0.6931471805599453
    return -1


if __name__ == '__main__':
    m=Mandelbrot(100,1000)
    img = get_escape_iter(m.c_val, m.N)
    from visualisation import show_image
    show_image(img, m.N)
