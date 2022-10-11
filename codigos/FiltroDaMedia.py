import cv2
import numpy as np
from .Utils import exibir_imagem

def filtro_da_media(img):
    y, z, rgb = img.shape

    out = np.zeros((y, z, rgb), dtype=np.uint8)

    for i in range(1, y-1):
        for u in range(1, z-1):
            for j in range(rgb):
                soma = img.item(i, u, j) + img.item(i-1, u-1, j) + img.item(i, u-1, j) + img.item(i+1, u-1, j) + img.item(i-1, u, j) + img.item(i+1, u, j) + img.item(i-1, u+1, j) + img.item(i, u+1, j) + img.item(i+1, u+1, j)
                out.itemset((i, u, j), soma/9)

    exibir_imagem(out, "filtro de media")
    
    return out