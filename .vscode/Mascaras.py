"""
É importante definir que uma mascara nada mais é que uma imagem onde cada pixel pode estar
"ligado" ou "desligado", ou seja, a máscara possui pixels pretos e branco apenas.
"""

# Importando bibliotecas
import cv2
import numpy as np
import imutils

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Abrindo imagem original
mascara = np.zeros(imagem.shape[:2], dtype="uint8")
(cX, cY) = (imagem.shape[1] // 2, imagem.shape[0] // 2)

# Fazendo o circulo na imagem
cv2.circle(mascara, (cX, cY), 100, 255, -1)

imagem_com_mascara = cv2.bitwise_and(imagem, imagem, mask=mascara)

# Abrindo a imagem
cv2.imshow('Mascara aplicada a imagem', imagem_com_mascara)
# Esperando apertar algo pra sair
cv2.waitKey(0)
