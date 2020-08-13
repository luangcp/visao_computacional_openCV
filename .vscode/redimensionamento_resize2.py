""" Outra maneira de redimensionar a imagem para tamanjos menores ou maiores
é utilizando a técnica de slicing. Neste caso é facil cortar pela metade o tamanho 
da imagem com o codigo abaixo: """

# Importando bibliotecas
import cv2
import imutils
import numpy as np

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Abrindo a imagem original
cv2.imshow('Original', imagem)

# Redimensionando a imagem
imagem_redimensionada = imagem[::2, ::2]

# Abrindo a nova imagem redimensionada
cv2.imshow('imagem redimensionada', imagem_redimensionada)
# Esperando apertar algo para fechar
cv2.waitKey(0)

""" O codigo basicamente refaz a imagem interpolando linhas e colunas
ou seja, pega a primeira linha, ignora a segunda, pega a terceira linha, ignora a quarta 
e assim por diante. O mesmo é feito com as colunas. Então temos uma imagem que é 
exatamente 1/4 da original """
