"""
Alterando um pouco a imagem abaixo. Veja que utilizamos os valores de linha multiplicado
pela coluna (x*y) no componente "g" da tupa que forma a cor de cada pixel e deixamos o componente 
azul e vermelho zerados. A dinamica da mudança de linhas e clunas gera esta imagem. 
"""
# Importando bibliotecas
import cv2
import imutils
import numpy as np

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Iniciando o laço for
for y in range(0, imagem.shape[0], 1):
    for x in range(0, imagem.shape[1], 1):
        imagem[y, x] = (0, (x*y) % 256, 0)

# ABRINDO A IMAGEM
cv2.imshow('Imagem modificada', imagem)
# ESPERANDO APERTAR ALGO PARA FECHAR
cv2.waitKey(0)
