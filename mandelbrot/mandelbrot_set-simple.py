import numpy as np
N = 50

def mandelbrot_set(c):
    z_old = 0
    for i in range(N):
        z = z_old**2 + c
        if abs(z) > 2:
            return i
        z_old = z
    return -1

def mandelbrot_img():
    d = 100
    x = 3*d
    y = (int) (4*d/3)
    img = np.zeros((y, x))
    c_val = np.zeros((x, y),dtype=np.complex128)
    for xi in range(x):
        for yi in range(y):
            cx = ((float) (xi/d -2 ))
            cy = ((float) (yi/d))
            c_val[xi,yi] = cx + cy*1j
    for xi in range(x):
        for yi in range(y):
            img[yi, xi] = mandelbrot_set(c_val[xi, yi])
    return img

if __name__ == '__main__':
    img = mandelbrot_img()
    from matplotlib import pyplot as plt
    plt.imshow(img)
    plt.show()
