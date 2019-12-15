import cv2
import numpy as np

if __name__ == "__main__":

    img = cv2.imread('android.png')
    img2 = cv2.imread('insta.png')

    y1, z1, rgb1 = img.shape
    y2, z2, rgb2 = img2.shape

    out = np.zeros((y1, z1, rgb1), dtype=np.uint8)

    cv2.imshow('imagem', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('imagem', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    for i in range(y1 - 1):
        for u in range(z1 - 1):
            for j in range(rgb1):
                x = img.item(i, u, j) + img2.item(i, u, j)
                if x < 255:
                    out.itemset((i, u, j), x)
                else:
                    out.itemset((i, u, j), 255)

    cv2.imshow('imagem', out)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


