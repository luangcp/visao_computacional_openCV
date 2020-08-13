"""
Também é possivel exibir os canais originais
"""
# Importando bibliotecas
import cv2
import numpy as np
import imutils

# Lendo a image
imagem = cv2.imread('imagem/ponte.jpg')

# Lendo os canais
(canalAzul, canalVerde, canalVermelho) = cv2.split(imagem)

# Matriz
zeros = np.zeros(imagem.shape[:2], dtype="uint8")  # Funciona como uma matriz
# Abrindo as imagens
cv2.imshow('Vermelho', cv2.merge([zeros, zeros, canalVermelho]))
cv2.imshow('Verde', cv2.merge([zeros, canalVerde, zeros]))
cv2.imshow('Azul', cv2.merge([canalAzul, zeros, zeros]))
cv2.imshow('Oriinal', imagem)
# Esperando apertar algo pra fechar
cv2.waitKey(0)
