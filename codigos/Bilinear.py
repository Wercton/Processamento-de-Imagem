import numpy as np
from .Utils import exibir_imagem


def bilinear_ampliar(img):
    y, x, rgb = img.shape

    out = np.zeros((y * 2, x * 2, rgb), dtype=np.uint8)

    for i in range(y):
        for u in range(x):
            for j in range(rgb):
                out.itemset((i * 2, u * 2, j), img.item(i, u, j))

    y, z, rgb = out.shape

    for i in range(y - 1):
        for u in range(z - 1):
            for j in range(rgb):
                if i % 2 == 0 and u % 2 == 0:
                    pass
                else:
                    if i % 2 == 0 and u % 2 != 0:
                        x = (out.item(i, u + 1, j) + out.item(i, u - 1, j)) // 2
                        out.itemset((i, u, j), x)
                    else:
                        if i % 2 != 0 and u % 2 == 0:
                            x = (out.item(i - 1, u, j) + out.item(i + 1, u, j)) // 2
                            out.itemset((i, u, j), x)
                        else:
                            x = (out.item(i + 1, u + 1, j) + out.item(i + 1, u - 1, j) + out.item(i - 1, u + 1, j) + out.item(i - 1, u - 1, j)) // 4
                            out.itemset((i, u, j), x)

    exibir_imagem(out, 'bilinear ampliagem')
    
    return out

def bilinear_reduzir(img):
    y, x, rgb = img.shape
    out = np.zeros((y // 2, x // 2, rgb), dtype=np.uint8)

    for i in range(y // 2):
        for u in range(x // 2):
            for j in range(rgb):
                z = (img.item(i * 2 + 1, u * 2, j) + img.item(i * 2, u * 2 + 1, j) + img.item(i * 2 + 1, u * 2 + 1, j) + img.item(i * 2, u * 2, j)) // 4
                out.itemset((i, u, j), z)

    
    exibir_imagem(out, 'bilinear reducao')

    return out
