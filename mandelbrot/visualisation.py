from matplotlib import pyplot as plt
from matplotlib.colors import LogNorm
import matplotlib as mpl

cmap = mpl.colormaps.get_cmap('rainbow')
cmap.set_bad(color='black')

def show_image(mb_img,N):
    fig, ax = plt.subplots()
    im = ax.imshow(mb_img, extent=[-2, 1, -4/3, 0], cmap=cmap, norm=LogNorm())
    ax.imshow(mb_img, extent=[-2, 1, 4/3, 0], cmap=cmap, norm=LogNorm())
    ax.set_aspect(1)
    ax.set_ylim([-4/3,4/3])
    fig.colorbar(im)
    plt.show()


if __name__ == '__main__':
    from mandelbrot_set import *
    m = Mandelbrot(10000,5000)
    img = m.mandelbrot_img()
    show_image(img, m.N)
