""" FATIAMENTO E DESENHO SOBRE IMAGEM
Também podemos utilizar a tecnica de slicing para altera varios pixels da imagem de uma 
unica vez como: imagem[30:50, :] = (255, 0, 0)
Esse codigo acima cria um retanfulo azul a partir da linha 31 até a linha 50 da imagem
e ocupa toda largura disponivel, ou seja, todas as colunas.
O codigo abaixo abre uma imagem e cria varios retangulos coloridos sobre ela
"""
# IMPORTANDO BIBLIOTECAS
import cv2
import numpy as np
import imutils

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# CRIA UM RETANGULO AZUL POR TODA LARGURA DA IMAGEM
imagem[30:50, :] = (255, 0, 0)

# CRIA UM QUADRADO VERMELHO
imagem[100:150, 50:100] = (0, 0, 255)

# CRIA UM RETANGULO AMARELO POR TODA ALTURA DA IMAGEM
imagem[:, 200:220] = (0, 255, 255)

# CRIA UM RETANGULO VERDE DA LINHA 150 A 300 NAS COLUNAS 250 A 350
imagem[150:300, 250:350] = (0, 255, 0)

# CRIA UM QUADRADO CIANO DA LINHA 150 A 300 NAS COLUNAS 250 A 350
imagem[300:400, 50:150] = (255, 255, 0)

# CRIA UM QUADRADO BRANCO
imagem[250:350, 300:400] = (255, 255, 255)

# CRIA UM QUADRADO PRETO
imagem[70:100, 300:450] = (0, 0, 0)

# ABRINDO AS IMAGENS
cv2.imshow('Imagem alterada', imagem)
# SALVANDO AS IMAGENS GERADAS
cv2.imwrite('Alterada.jpg', imagem)
# Esperando apertar algo para fechar
cv2.waitKey(0)
