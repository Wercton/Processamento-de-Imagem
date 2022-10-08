import cv2
from codigos import soma, subtracao


def menu_inicial():
    while True:
        print('0 - sair')
        print('1 - ver imagens')
        print('2 - realizar soma')
        print('3 - realizar subtração')
        x = input('Digite seu comando: ')

        if x == '0':
            break
        elif x == '1':
            exibir_imagens()
        elif x == '2':
            soma()
        elif x == '3':
            subtracao()
        
        print('\n\n\n')

def exibir_imagens():
    img = cv2.imread('./imagens/imagem1.png')
    img2 = cv2.imread('./imagens/imagem2.png')
    
    cv2.imshow('imagem1', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imshow('imagem2', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    menu_inicial()