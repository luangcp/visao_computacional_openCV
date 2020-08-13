""" Nesse codigo incluimos as variaveis de linha e coluna
para serem as componentes de cor, lembrando que as variaveis componentes
da cor devem assumir o valor entre 0 e 255, então utilizamos a operação
" resta da divisao por 256" para manter o resultado entre 0 e 255"""

# Incluindo bibliotecas
import cv2
import imutils
import numpy as np

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Iniciando o laço de repetição for in range (varrendo)
for y in range(0, imagem.shape[0]):  # Percorrendo as linhas
    for x in range(0, imagem.shape[1]):  # Percorrendo as coluns
        # Fazendo o resto da divisão para manter o resultado entre o e 255
        imagem[y, x] = (x % 256, y % 256, x % 256)

# ABRINDO A IMAGEM
cv2.imshow('Imagem modificada', imagem)
# Esperando apertar algo
cv2.waitKey(0)
