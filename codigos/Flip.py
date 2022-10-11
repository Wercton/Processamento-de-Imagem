import numpy as np
from .Utils import exibir_imagem


def flip_vertical(img):

    y, z, rgb = img.shape
    out = np.zeros((y, z, rgb), dtype=np.uint8)

    for i in range(y):
        for u in range(z):
            for j in range(rgb):
                out.itemset((i, u, j), img.item(i * -1, u * -1, j))

    exibir_imagem(out, 'flip vertical')
    
    return out


def flip_horizontal(img):
    y, z, rgb = img.shape
    out = np.zeros((y, z, rgb), dtype=np.uint8)

    for i in range(y):
        for u in range(z):
            for j in range(rgb):
                out.itemset((i, u, j), img.item(i, u * -1, j))

    exibir_imagem(out, 'flip horizontal')
    
    return out