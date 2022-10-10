import cv2
import numpy as np


def flip_vertical(img):

    y, z, rgb = img.shape
    out = np.zeros((y, z, rgb), dtype=np.uint8)

    for i in range(y):
        for u in range(z):
            for j in range(rgb):
                out.itemset((i, u, j), img.item(i * -1, u * -1, j))

    cv2.imshow('imagem', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return out


def flip_horizontal(img):
    y, z, rgb = img.shape
    out = np.zeros((y, z, rgb), dtype=np.uint8)

    for i in range(y):
        for u in range(z):
            for j in range(rgb):
                out.itemset((i, u, j), img.item(i, u * -1, j))

    cv2.imshow('imagem', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return out