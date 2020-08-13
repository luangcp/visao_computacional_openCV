"""
A mediana é semelhante a media, mas ela despreza valores muito altos ou muito baixos que podem distorcer 
o resultado. A mediana é o número que fica exatamente no meio do intervalo.

A função utilizada é a cv2.mediamBlur(imagem, 3) e o unico argumento é o tamanho da caixa ou janela usada

é importante notar que este metodo n cria novas cores, como pode acontecer com os anteriores
ele sempre altera a cor do pixel atual com um dos valores da vizinhança.
"""
# Importando bibliotecas
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Diminuindo a imagem
imagem = imagem[::2, ::2]

# Suavizando a imagem pela mediana
suave = np.vstack([
    np.hstack([imagem, cv2.medianBlur(imagem, 3)]),
    np.hstack([cv2.medianBlur(imagem, 5), cv2.medianBlur(imagem, 7)]),
    np.hstack([cv2.medianBlur(imagem, 9), cv2.medianBlur(imagem, 11)]),
])

# Abrindo as imagens
cv2.imshow('Imagem original e suavizadas pela mediana', suave)

# Esperando apertar algo para fechar
cv2.waitKey(0)
