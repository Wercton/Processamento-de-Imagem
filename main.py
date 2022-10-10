import cv2
from codigos import *


if __name__ == "__main__":
    img1 = cv2.imread('./imagens/imagem1.png')
    img2 = cv2.imread('./imagens/imagem2.png')
    
    soma(img1, img2)
    subtracao(img1, img2)

    VizinhoMaisProximo.vizinho_mais_proximo_ampliar(img1)
    VizinhoMaisProximo.vizinho_mais_proximo_reduzir(img1)

    Bilinear.bilinear_ampliar(img1)
    Bilinear.bilinear_reduzir(img1)