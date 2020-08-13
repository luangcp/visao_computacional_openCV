"""
Em inglês canny pode ser traduzido para esperto, E o carry Hedge
Detector ou detector de bordas caany realmente é mais inteligente que os outros.
Ele se utiliza de outras tecnicas como o Sobel e realiza multiplos passos para
chegar ao resultado final.

Basicamente o Canny envolve:
1 - Aplicar um filtro gaussiano para suavizar a imagem e remover o ruido
2 - Encontrar os gradientes de intensidade da imagem
3 - Aplicar sobel duplo para determinar bordas potenciais.
4 - Aplicar o processo de "Hysteresis" para verificar se o pixel faz parte
de uma borda "forte" suprimindo todas as outras bordas que são fracas
e não conectadas a bordas fortes.

É preciso fornecer dois parametros para a função cv2.canny(). Esses dois valores 
são o limiar 1 e o limiar 2 e são utilizados no processo de hysteresis final. Qualquer
gradiente com valor maior que o limiar 2 é considerado como borda. Qualquer valor inferior ao
limiar 1 não é considerado como borda. Valores entre o limiar 1 e o limiar 2 são classificados 
como bordas ou não bordas com base em como eles são conectados
"""
# Importando bibliotecas
import cv2
import numpy as np
import imutils
import mahotas
from matplotlib import pyplot as plt

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Convertando para preto e branco
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Suavizando a imagem com GaussianBlur
suave = cv2.GaussianBlur(imagem, (7, 7), 0)

# Aplicando o metodo Canny
canny1 = cv2.Canny(suave, 20, 120)
canny2 = cv2.Canny(suave, 70, 200)

# Juntando tudo em uma imagem
resultado = np.vstack([
    np.hstack([imagem, suave]),
    np.hstack([canny1, canny2])
])

# Abrindo a imagem
cv2.imshow('Detector de bordas Canny', resultado)
# Esperando apertar algo para fechar
cv2.waitKey(0)
