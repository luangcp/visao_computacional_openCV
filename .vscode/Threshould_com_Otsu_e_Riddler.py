"""
Outro metodo que automaticamente encontra um threshould para a imagem é o metodo
de Otsu. Neste caso ele analiza o histograma da imagem para encontrar os dois maiores picos
de intensidades, então ele calcula um valor para separar da melhor forma esses dois picos.
"""
# Importando bibliotecas
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt
import mahotas


# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Convertendo em preto e branco
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Suavizando a imagem com Gaussian
suave = cv2.GaussianBlur(imagem, (7, 7), 0)  # Aplica o blur

# Metodo OTSU
T = mahotas.thresholding.otsu(suave)
temp = imagem.copy()
temp[temp > T] = 255
temp[temp < 255] = 0
temp = cv2.bitwise_not(temp)

# Metodo Riddler Calvard
T = mahotas.thresholding.rc(suave)
temp2 = imagem.copy()
temp2[temp2 > T] = 255
temp2[temp2 < 255] = 0
temp2 = cv2.bitwise_not(temp2)

# TUDO NUMA MESMA IMAGEM
resultado = np.vstack([
    np.hstack([imagem, suave]),  # Primeira linha com essas imagens
    np.hstack([temp, temp2])  # Segunda linha com essas imagens
])

# ABRINDO A IMAGEM
cv2.imshow('Binirizacao com metodo Otsu e Riddler-Calvard', resultado)

# Esperando apertar algo para fechar
cv2.waitKey(0)
