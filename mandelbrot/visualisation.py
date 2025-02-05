from matplotlib import pyplot as plt
import numpy as np
def show_image(mb_img):
    fig, ax = plt.subplots()
    ax.imshow(mb_img, extent=[-2, 1, -4/3, 0])
    ax.imshow(mb_img, extent=[-2, 1, 4/3, 0])
    ax.set_aspect(1)
    ax.set_ylim([-4/3,4/3])
    plt.show()


if __name__ == '__main__':
    from mandelbrot_set import mandelbrot_img
    img = mandelbrot_img()
    show_image(img)