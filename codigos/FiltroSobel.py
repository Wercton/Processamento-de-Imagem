import cv2
import numpy as np
from .Utils import exibir_imagem


def sobel(img):
    y, z, r = img.shape

    out = filtros([[-1, -2, -1], [0, 0, 0], [1, 2, 1]], img)
    out2 = filtros([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]], img)
    
    # exibir_imagem(out, 'horizontal')
    # exibir_imagem(out2, 'vertical')

    for i in range(y - 1):
        for u in range(z - 1):
            for j in range(r):
                x = out.item(i, u, j) + out2.item(i, u, j)
                if x < 255:
                    out.itemset((i, u, j), x)
                else:
                    out.itemset((i, u, j), 255)
    
    exibir_imagem(out, 'filtro sobel')
    return out


def filtros(A, img):
    y, z, r = img.shape
    out = np.zeros((y, z, r), dtype=np.uint8)

    for i in range(1, y - 1):
        for u in range(1, z - 1):
            for j in range(r):
                valor = A[0][0] * img.item(i-1, u-1, j) + A[0][1] * img.item(i, u-1, j) + A[0][2] * img.item(i+1, u-1, j) + A[1][0] * img.item(i-1, u, j) + A[1][1] * img.item(i, u, j) + A[1][2] * img.item(i+1, u, j) + A[2][0] * img.item(i-1, u+1, j) + A[2][1] * img.item(i, u+1, j) + A[2][2] * img.item(i+1, u+1, j)
                if valor > 255:
                    valor = 255
                elif valor < 0:
                    valor = 0
                out.itemset((i, u, j), valor)

    return out

# (a) [[0, 1, 0], [1, -4, 1], [0, 1, 0]]
# (b) [[1, 1, 1], [1, -8, 1], [1, 1, 1]]
# (c) [[0, -1, 0], [-1, 4, -1], [0, -1, 0]]
# (d) [[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]]
