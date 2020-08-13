""" Sistema de coordenadas e manipulação de pixels
Temos uma representação de 3 cores no sistema RGB para cada pixel da imagem colorida
Podemos alternar a cor individualmente para cada pixel, ou seja
podemos manipular individualmente cada pixel da imagem. """

""" 
É importante entender o sistema de coordenadas (linha , coluna) onde o pixel mais a esquerda e acima da imagem
estão na posição (0,0) esta na linha 0 e coluna 0. Já em uma imagem com 300 pixels de largura, ou seja,
300 colunas e tendo 200 pixels de altura, ou seja, 200 linhas terá o pixel mais a direita e abaixo 
da imagem 
"""
# É possivel alterar individualmente cada pixel ou ler a informação individual do pixel

# Importando bibiotecas

# Lendo a imagem
import cv2
import imutils
import numpy as np
imagem = cv2.imread('imagem/ponte.jpg')
(b, g, r) = imagem[0, 0]  # VEJA QUE A ORDEM É BGR E NÃO RGB

""" Imagens são matrizes Numpy, neste caso retornadas pelo metodo "imread" e armazenada
através da variavel imagem. """

print('O pixel (0,0) tem as ;seguintes cores:')
print('Vermelho:', r, "Verde", g, 'Azul: ', b)

# O pixel (0,0) tem as seguintes cores: Vermelho 124, Verde 155, Azul 186
