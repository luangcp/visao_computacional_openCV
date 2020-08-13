""" Outro exemplo utilização de mascaras"""
# Importando bibliotecas
import cv2
import numpy as np
import imutils

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Abrindo a imagem original
cv2.imshow('Original', imagem)

# Criando a mascara
mascara = np.zeros(imagem.shape[:2], dtype='uint8')

(cX, cY) = (imagem.shape[1] // 2, imagem.shape[0] // 2)

cv2.circle(mascara, (cX, cY), 180, 255, 70)
cv2.circle(mascara, (cX, cY), 70, 255, -1)

# gERANDO A IMAGEM
cv2.imshow("Mascara", mascara)

imagem_com_mascara = cv2.bitwise_and(imagem, imagem, mask=mascara)
# Abrindo imagem da mascara aplicada a imagem
cv2.imshow('Mascara aplicada a imagem', imagem_com_mascara)
# Esperando apertar algo para fechar
cv2.waitKey(0)
