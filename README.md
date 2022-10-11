<h1 align="center"> Processamento de Imagem </h1>
<p align="center">
  <img src="./resultados/soma.jpg" width="200">
</p>

## :spiral_notepad: Descrição do projeto

Este projeto constitui um conjunto dos códigos realizados para a matéria de Processamento de Imagem, ministrada pela Dra. Glenda Michele Botelho, enquanto estudante do curso de Ciência da Computação na Universidade Federal do Tocantins (UFT).

## 🔨 Ferramentas usadas

- ``Python 3.8.10``
- ``Numpy 1.23.3``
- ``OpenCV 4.6.0.66``
- ``Matplotlib 3.6.1``

## Rodando o projeto

Os algoritmos de manipulação de imagem estão dispersos dentro da pasta `./codigos/`, para usá-los basta chamá-los na main do projeto. As imagens usadas podem ser alteradas, bastando substituí-las na pasta `./imagens/`, sendo **NECESSÁRIO** garantir que tanto a `imagem1` tenha o mesmo tamanho que a `imagem2`.

Para instalar as depedências do projeto (recomendável que o faça dentro de um [ambiente virtual](https://docs.python.org/pt-br/3/tutorial/venv.html)), rode o seguinte comando no terminal:
```
pip install -r requirements.txt
```

As imagens resultantes não são naturalmente salvas, mas caso deseje salvá-las, a seguinte função do `OpenCV` pode ser utilizada dentro do código:
```
cv2.imwrite('./resultados/{nome do arquivo}.jpg', {função da qual deseja salvar o resultado})
```
Exemplo:
```
cv2.imwrite('./resultados/soma.jpg', soma(img1, img2))
```

## ✔️ Funcionalidades
- [Filtro da média](https://github.com/Wercton/Processamento-de-Imagem/blob/master/codigos/FiltroDaMedia.py)
- [Filtro sobel](https://github.com/Wercton/Processamento-de-Imagem/blob/master/codigos/FiltroSobel.py)
- [Flip vertical e horizontal](https://github.com/Wercton/Processamento-de-Imagem/blob/master/codigos/Flip.py)
- [Interpolação bilinear](https://github.com/Wercton/Processamento-de-Imagem/blob/master/codigos/Bilinear.py)
- [Interpolação por vizinho mais próximo](https://github.com/Wercton/Processamento-de-Imagem/blob/master/codigos/VizinhoMaisProximo.py)
- [Histograma](https://github.com/Wercton/Processamento-de-Imagem/blob/master/codigos/Histograma.py)
- [Soma de imagens](https://github.com/Wercton/Processamento-de-Imagem/blob/master/codigos/Soma.py)
- [Subtração de imagens](https://github.com/Wercton/Processamento-de-Imagem/blob/master/codigos/Subtracao.py)
- [Transformação de Intensidade](https://github.com/Wercton/Processamento-de-Imagem/blob/master/codigos/TransformacaoDeIntensidade.py)