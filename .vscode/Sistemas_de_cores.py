""" Ja conhecemos o tradicional espaço de cores RGB(red, green, blue) que sabemos que em openCV
é retratado por BGR dada a necessidade de colocar o azul como primeiro elemento e  vermelho como 
terceiro elemento de uma tpla que compoe as cores de pixel.

Contudo exeistem outros espaços de cores como o proprio " Preto e Branco" ou " Tons de cinza", alem
de outros coloridos como o L*aB* e o HSV
"""
# Importando bibliotecas
import cv2
import imutils
import numpy as np

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Lendo os canais de cores
(canalAzul, canalVerde, canalVermelho) = cv2.split(imagem)

# Abrindo as imagens
cv2.imshow('Vermelho', canalVermelho)
cv2.imshow('Verde', canalVerde)
cv2.imshow('Azul', canalAzul)
# Esperando apertar algo para fechar
cv2.waitKey(0)

"""
A função split faz o trabalho duro separando os canais. Assim podemos exibi-los em
tons de cinza conforme mostram as imagens
"""
