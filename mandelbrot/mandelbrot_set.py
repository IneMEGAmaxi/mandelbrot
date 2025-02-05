import numpy as np
from math import log

class Mandelbrot:
    xmin = -2; xmax = 1; ymin = 0; ymax = 4/3
    def __init__(self, max_iter, pixel_density):
        self.N = max_iter
        self.d = pixel_density
        self.c_val = self.get_c_val()
    
    def get_c_val(self):
        x = np.linspace(self.xmin, self.xmax, int((self.xmax-self.xmin)*self.d))
        y = np.linspace(self.ymin, self.ymax, int((self.ymax-self.ymin)*self.d))
        X, Y = np.meshgrid(x,y)
        return X + Y*1j
    
    def mandelbrot_img(self):
        img = np.zeros(self.c_val.shape)
        for (i, j), c in np.ndenumerate(self.c_val):
            img[i,j] = self.escape_iter(c)
        return img
    
    def escape_iter(self, c):
        z_old = 0
        for i in range(self.N):
            z = z_old**2 + c
            if abs(z) > 2:
                return i + 1 - log(log(abs(z))) / log(2)
            z_old = z
        return -1


if __name__ == '__main__':
    img = Mandelbrot(100,1000).mandelbrot_img()
    #from visualisation import show_image
    #show_image(img)
