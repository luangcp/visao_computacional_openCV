""" Para reduzir ou aumentar o tamanho da imagem, existe uma função já
pronta kda OpenCV, trata-se da função resize. 
IMPORTANTE notar que é preciso calcular a proporção da altura em relação
a largura da nova imagem, caso contrário ela poderá ficar distorcida """

# Importando bibliotecas
import cv2
import numpy as np
import imutils

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Abrindo a imagem original
cv2.imshow('Original', imagem)

# Determinando altura e larguta
largura = imagem.shape[1]
altura = imagem.shape[0]

# Determinadno a proporção (calculo pra n ficar distorcida) da imagem
proporcao = float(altura/largura)

# Determinado largura nova
largura_nova = 320  # em pixels
# Determinando altura nova
altura_nova = int(largura_nova*proporcao)

# Determinando tamanho novo
tamanho_novo = (largura_nova, altura_nova)

imagem_redimensionada = cv2.resize(
    imagem, tamanho_novo, interpolation=cv2.INTER_AREA)

cv2.imshow('Resultado', imagem_redimensionada)
cv2.waitKey(0)

""" Veja que na funçao resize utiliza uma propriedade aqui definida como cv2.INTER_AREA que é uma especificação
do calculo matematico para redimensionar a imagem. Apesar dsso, caso a imagem seja redimensionada para um tamanho maior
é preciso ponderar que ocorrerá perde de qualidade
"""
