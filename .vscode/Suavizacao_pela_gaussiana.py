"""
Ao invés do filtro de caixa é utilizado um kernel gaussiano. Isso é calculado através da função
cv2.GaussianBlur(). A função exige especificação de uma largura e altura com números impares e 
também, opcionalmente, é possivel especificar a quantidade de desvios padrão no eixo X e Y (horizntal e vertical)
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

# Suavizando em uma unica imagem
suave = np.vstack([
    np.hstack([imagem, cv2.GaussianBlur(imagem, (3, 3), 0)]),
    np.hstack([cv2.GaussianBlur(imagem, (5, 5), 0),
               cv2.GaussianBlur(imagem, (7, 7), 0)]),
    np.hstack([cv2.GaussianBlur(imagem, (9, 9), 0),
               cv2.GaussianBlur(imagem, (11, 11), 0)]),
])

# Abrindo a imagem
cv2.imshow("Imagem original e suavisadas pelo filtro gaussiano", suave)

# Esperando apertar algo para fechar
cv2.waitKey(0)

"""
OBS: O filtro kernel gaussiano gera menos borrao na imagem mas também gera
um efeito natual e reduz o ruido na imagem.
"""
