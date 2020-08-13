"""
Uma das mais famosas transformações na geometria que também é utilizada em processamento de imagem se 
chama affine

A transformação affine ou mapa affine é uma função entre espaços affine que preservam os pontos
grossura de linhas e planos. Além disso, linhas paralelas permancecem paralelas após uma transformação affine.

Essas transformções não necessariamente preservam a distancia entre pontos mas ela preserva a proporção
das distancias entre os pontos de uma linha reta. Uma rotação é um tipo de transformação affine.
"""

# Bibliotecas
import cv2
import imutils
import numpy as np

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Captando altura e largura
(alt, lar) = imagem.shape[:2]

# Achando o centro
centro = (lar // 2, alt // 2)

M = cv2.getRotationMatrix2D(centro, 30, 1.0)  # CENTRO ANGULO E ESCALA

imagem_rotacionada = cv2.warpAffine(imagem, M, (lar, alt))

# Abrindo a imagem
cv2.imshow('Imagem rotacionada em 45 graus', imagem)
# So fecha quando apertar algo
cv2.waitKey(0)
