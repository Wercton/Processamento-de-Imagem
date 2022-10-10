import cv2


def exibir_imagem(img, descricao='imagem'):
    cv2.imshow(descricao, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()