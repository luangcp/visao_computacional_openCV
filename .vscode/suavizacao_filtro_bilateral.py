"""
Esse metodo é mais lento para calcular do que os anterores mas como vantagem apresenta
preservação de bordas e garante que o ruido seja removido.

Para realiza isso, alem de um filtro gaussiano do espaço ao redor do pixel,
também é utilizado outro cálculo com outro filtro gaussiano que leva
em conta a diferença de intensidade entre os pixels, dessa forma, como resultado
temos uma maior manutenção das bordas das imagens. A função usada é cv2.bilateralFilter()
"""
# Importando bibliotecas
import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Diminuindo a imagem
imagem = imagem[::2, ::2]

# Suavizando com o filtro bilateral
suave = np.vstack([
    np.hstack([imagem, cv2.bilateralFilter(imagem, 3, 21, 21)]),
    np.hstack([cv2.bilateralFilter(imagem, 5, 35, 35),
               cv2.bilateralFilter(imagem, 7, 49, 49)]),
    np.hstack([cv2.bilateralFilter(imagem, 9, 63, 63),
               cv2.bilateralFilter(imagem, 11, 77, 77)]),
])

# Abrindo as imagens
cv2.imshow('Imagem original e suavizadas com filtro bilateral', suave)

# Esperando apertar algo para fechar
cv2.waitKey(0)
