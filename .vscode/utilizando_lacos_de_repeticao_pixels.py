""" Outra possibilidade é utilizar dois laços de repetição para "varrer" todos os pixels da imagem
linha por linha, como é o caso do codigo abaixo:"""
# Obs: Essa estrategia pode nao ser muit perfomatica ja que é um processo lento varrer toda a imagem pixel a pixel

# Importando bibliotecas
import cv2
import imutils
import numpy as np

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Iniciando o laço for in range que percorre as linhas
for y in range(0, imagem.shape[0]):  # Percorre linhas
    for x in range(0, imagem.shape[1]):  # Percorre colunas
        imagem[y, x] = (255, 0, 0)

# ABRINDO A IMAGEM
cv2.imshow("Imagem modificada", imagem)

# Esperando apertar algo para fechar
cv2.waitKey(0)
