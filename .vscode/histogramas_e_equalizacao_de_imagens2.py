"""
Além do histograma da imagem em tons de cinza é possivel plotar um histograma da 
imagem colorida.
Nesse caso teremos três linhas, uma para cada canal.
Importante notar que a função zip cria uma lista de tuplas formada pela união das listas
passadas e não tem nada haver com um processo de compactaçao como poderia se esperar
"""
# Importando bibliotecas
import cv2
from matplotlib import pyplot as plt
import imutils
import numpy as np

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')
# Abrindo imagem
cv2.imshow('Imagem colorida', imagem)

# Separando os canais
canais = cv2.split(imagem)
cores = ("b", "g", "r")
plt.figure()  # Lendo a figura
plt.title('Histograma colorido')  # TITULO DO HISTOGRAMA
plt.xlabel('Intensidade')  # Nome do eixo x
plt.ylabel('Numero de pixels')  # Nome do eixo y

# Laço for para varrer
for (canal, cor) in zip(canais, cores):
    # ESTE LOOP EXECUTA 3 VEZES, UMA PARA CADA CANAL
    hist = cv2.calcHist([canal], [0], None, [256], [0, 256])
    plt.plot(hist, cor=cor)
    plt.xlim([0, 256])
plt.show()
# ESperando apertar algo para sair
