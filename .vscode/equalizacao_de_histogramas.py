""" É possivel realizar um calculo matematico sobre a distribuição de pixels para aumentar o contraste da imagem.
A intensão nesse caso é distribuir de forma mais uniforma as intensidaes ds pixels sobre a imagem.
No histograma é possivel identificar a diferença pois o acumulo de pixels proximo a alguns valores é suavizado.
Veja a diferença entre o histrograma original e o equalizado abaixo: """
# Importando bibliotecas
import cv2
from matplotlib import pyplot as plt
import numpy as np
import imutils

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')


imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Equalizando
h_eq = cv2.equalizeHist(imagem)

# Plotando o grafico
plt.figure()
plt.title('Histograma equalizado')
plt.xlabel('Intensidade')
plt.ylabel('Qtde de Pixels')
plt.hist(h_eq.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

# Mostrando o original não equalizado
plt.figure()
plt.title('Histograma original')
plt.xlabel('Intensidade')
plt.ylabel('Qtde de pixels')
plt.hist(imagem.ravel(), 256, [0, 256])
plt.xlim([0, 256])
plt.show()

# Esperando apertar algo para fechar
cv2.waitKey(0)
