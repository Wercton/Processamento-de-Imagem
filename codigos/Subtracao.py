import cv2
import numpy as np
from .Utils import exibir_imagem

def subtracao(img1, img2):
    y1, z1, rgb1 = img1.shape

    out = np.zeros((y1, z1, rgb1), dtype=np.uint8)

    for i in range(y1 - 1):
        for u in range(z1 - 1):
            for j in range(rgb1):
                x = img1.item(i, u, j) + img2.item(i, u, j)
                if x > 0:
                    out.itemset((i, u, j), x)
                else:
                    out.itemset((i, u, j), 0)

    exibir_imagem(out, 'subtracao')

    return out