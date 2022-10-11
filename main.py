import cv2
from codigos import *


if __name__ == "__main__":
    img1 = cv2.imread('./imagens/imagem1.png')
    img2 = cv2.imread('./imagens/imagem2.png')
    
    # exibir_imagem(img1, "imagem 1")
    # exibir_imagem(img2, "imagem 2")
    
    #? cv2.imwrite('./resultados/soma.jpg', soma(img1, img2))
    
    # soma(img1, img2)
    # subtracao(img1, img2)
    # flip_vertical(img1)
    # flip_horizontal(img1
    # vizinho_mais_proximo_ampliar(img1)
    # vizinho_mais_proximo_reduzir(img1)
    # bilinear_ampliar(img1)
    # bilinear_reduzir(img1)
    # transformacao_pot(img2)
    # transformacao_log(img2)
    # histograma(img1, contraste=2)  # 0, 1 ou 2
    # filtro_da_media(img1)
    # sobel(img2)