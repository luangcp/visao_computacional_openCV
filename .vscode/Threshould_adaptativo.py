"""
É possivel otimizar o valor de intensidade matematicamente, esta é a proposta do threshould adaptativo
Para isso precisamos dar um valor da janela ou caixa de cálculo para que o limiar seja calculado no pixels
proximos das imagens. Outro parâmetro é um inteiro que é subtraido da média calculada dentro da caixa
para gerar o threshoul final.
"""
# Importando bibliotecas
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')
# Convertento em preto e branco
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Suavizando a imagem com Gaussian
suave = cv2.GaussianBlur(imagem, (7, 7), 0)  # Aplica o blur

bin1 = cv2.adaptiveThreshold(
    suave, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY_INV, 21, 5)

bin2 = cv2.adaptiveThreshold(
    suave, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 5)

resultado = np.vstack([
    np.hstack([imagem, suave]),
    np.hstack([bin1, bin2])
])

# Abrindo a imagem
cv2.imshow('Binarização adaptativa de imagem', resultado)
# Esperando apertar algo para fechar
cv2.waitKey(0)
