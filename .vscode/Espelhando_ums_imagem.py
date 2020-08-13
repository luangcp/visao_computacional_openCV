""" Para espelhar uma imagem, basta inverter suas linhas, suas colunas ou ambar.
Invertendo as linhas temos o flip horizontal e invertendo as colunas temos o flip vertical"""

""" Podemos fazer o espelhamento/flip com uma função oferecida pela OPENCV (função flio) como através da
manipulação direta das matrizes que compõe a imagem."""

# Importando as bibliotecas

# lendo a imagem
import cv2
import imutils
import numpy as np
imagem = cv2.imread('imagem/ponte.jpg')
# Abrindo a imagem original
cv2.imshow('Original', imagem)

# Fazendo o flip
flip_horizontal = imagem[::-1, :]
# Outro comando equivalete
# flip_horizontal = cv2.flip(imagem, 1)

# Abrindo a imagem com o flip horizontal
cv2.imshow("Flip Horizontal", flip_horizontal)

# Flip vertical
flip_vertical = imagem[:, ::-1]
# Outro comando equivalente
# flip_vertical = cv2.flip(imagem, 0)

# Abrindo a imagem vertical
cv2.imshow('Flip Vertical', flip_vertical)
# Fazendo o flip horizontal e vertical
flip_hv = imagem[::-1, ::-1]
# flip_hv = cv2.flip(imagem, -1)

# Abrindo imagem do flip horizontal e vertical
cv2.imshow("Flip horizontal e Vertical", flip_hv)
cv2.waitKey(0)
