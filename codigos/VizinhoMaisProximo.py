import numpy as np
from .Utils import exibir_imagem


def vizinho_mais_proximo_ampliar(img):
    y, x, rgb = img.shape
    out = np.zeros((y * 2, x * 2, rgb), dtype=np.uint8)

    for i in range(y):
        for u in range(x):
            for j in range(rgb):
                out.itemset((i * 2, u * 2, j), img.item(i, u, j))

    # cv2.imshow('vizinho mais proximo', out)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    for i in range(2, y * 2):
        for u in range(2, x * 2):
            for j in range(rgb):
                if i % 2 == 0 and u % 2 == 0:
                    continue
                else:
                    if i % 2 == 0 and u % 2 != 0:
                        out.itemset((i, u, j), out.item(i, u - 1, j))
                    else:
                        if i % 2 != 0 and u % 2 == 0:
                            out.itemset((i, u, j), out.item(i - 1, u, j))
                        else:
                            out.itemset((i, u, j), out.item(i - 1, u - 1, j))

    exibir_imagem(out, 'vizinho mais proximo ampliagem')
    
    return out

def vizinho_mais_proximo_reduzir(img):
    y, x, rgb = img.shape
    out = np.zeros((y // 2, x // 2, rgb), dtype=np.uint8)

    for i in range(y // 2):
        for u in range(x // 2):
            for j in range(rgb):
                out.itemset((i, u, j), img.item(i * 2, u * 2, j))

    exibir_imagem(out, 'vizinho mais proximo reducao')
    
    return out
