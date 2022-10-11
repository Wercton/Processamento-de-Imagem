import cv2
import math
import numpy as np

from codigos.Utils import exibir_imagem


def transformacao_log(img):
    y, z, rgb = img.shape

    out = np.zeros((y, z, rgb), dtype=np.uint8)

    c = 100
    # s = c * math.log10(1 + r)

    for i in range(y):
        for u in range(z):
            for j in range(rgb):
                r = img.item(i, u, j)
                s = c * math.log10(1 + r)
                if s > 255:
                    out.itemset((i, u, j), 255)
                else:
                    out.itemset((i, u, j), s)

    exibir_imagem(out)
    
    return out

def transformacao_pot(img):

    y, z, rgb = img.shape
    out = np.zeros((y, z, rgb), dtype=np.uint8)

    c = 1
    y1 = 1

    for i in range(y):
        for u in range(z):
            for j in range(rgb):
                r = img.item(i, u, j)/255
                s = c * (r**y1)
                if s > 255:
                    out.itemset((i, u, j), 255)
                else:
                    out.itemset((i, u, j), s*255)

    exibir_imagem(out)
    
    return out
