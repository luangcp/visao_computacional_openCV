""" O objetivo agora é saltar a cada 10 pixels
ao percorrer as linhas e mais 10 pixels ao percorrer as colunas.
A cada salto é criado um quadrado amarelo de 5x5 pixels. Desta vez
parte da imagem oriinal é preservada e podemos ainda 
observar a ponte por baixo da grade de quadrados amarelos
"""
# Importando bibliotecas
import cv2
import imutils
import numpy as np

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Iniciando o laço for in range para percorrer
for y in range(0, imagem.shape[0], 10):
    for x in range(0, imagem.shape[1], 10):
        imagem[y:y+5, x:x+5] = (0, 255, 255)

# ABRINDO A IMAGEM
cv2.imshow('Imagem modificada', imagem)
# ESPERANDO APERTAR ALGO PARA FECHAR
cv2.waitKey(0)
