""" COM A TECNICA SLICING É POSSIVEL CRIAR QUADRADOS E RETANGULOS, contudo, para outras
forma geometricas é possivel utilizar as funções da OPENCV, isso é util principalmente no
caso de desenho de circulos e textos sobre a imagem, veja:
"""

# IMPORTANDO BIBLIOTECAS
import cv2
import numpy as np
import imutils

# LENDO A IMAGEM
imagem = cv2.imread('imagem/ponte.jpg')

vermelho = (0, 0, 255)
verde = (0, 255, 0)
azul = (255, 0, 0)

# CRIANDO LINHAS
cv2.line(imagem, (0, 0), (100, 200), verde)
cv2.line(imagem, (300, 200), (150, 150), vermelho, 5)

# CRIANDO RETANGULOS
cv2.rectangle(imagem, (20, 20), (120, 120), azul, 10)
cv2.rectangle(imagem, (200, 50), (225, 125), verde, -1)

(X, Y) = (imagem.shape[1] // 2, imagem.shape[0] // 2)
for raio in range(0, 175, 15):
    cv2.circle(imagem, (X, Y), raio, vermelho)

# ABRINDO A IMAGEM
cv2.imshow("DESENHANDO SOBRE A IMAGEM", imagem)
# ESPERANDO APERTAR ALGO PARA FECHAR
cv2.waitKet(0)
