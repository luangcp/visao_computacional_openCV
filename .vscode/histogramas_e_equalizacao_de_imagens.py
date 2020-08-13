"""
Um histrograma é um grafico de colunas ou de lihas que representa a distribuição dos
valores dos pixels de uma imagem, ou seja, a quantidade de pixeis mais claros (proximos de 255)
e a quantidade de pizels mais escuros (proximos de 0)

O eixo X do grafico normalmente possui uma distribuição de 0 a 255 ue demostra o valor (intensidade) do pixel
No eixo y do pixel é plotada a quantidade de pixels daquela intesidade
"""
# Demonstrando histograma
# Importando bibliotecas
import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')
# Convertando em Preto e branco
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
# Abrindo imagem convertida
cv2.imshow('Imagem PeB', imagem)

# FUNÇÃO CALCHIST PARA CALCULAR O HISOGRAMA DA IMAGEM
h = cv2.calcHist([imagem], [0], None, [256], [0, 256])

# MATPLOTLIB
# GERANDO O HISTROGRAMA
plt.figure()
plt.title("Histograma P&B")  # TITULO DO HISTOGRAMA
plt.xlabel("Intensidade")  # Nome do eixo X
plt.ylabel('Quantidade de pixels')  # Nome do eixo Y
plt.plot(h)  # PLOTANDO O HISTOGRAMA
plt.xlim([0, 256])
plt.show()

# SO FECHA QUANDO APERTAR ALGO
cv2.waitKey(0)
