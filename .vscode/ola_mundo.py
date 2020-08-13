""" Primeiro programa advindo do livro visão computacional e openCV com python """

# Importando as bibliotecas
import cv2  # biblioteca openCV
import imutils  # Biblioteca imutils
import matplotlib  # Importando matplotlib

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Vendo a largura da imagem
print('Largura em pixels:', end='')
print(imagem.shape[1])  # LARGURA DA IMAGEM
# Vendo a altura da imagem
print('Altura em pixels: ', end='')
print(imagem.shape[0])  # ALTURA DA IMAGEM

# ABRINDO A IMAGEM
# OBS: SEMPRE PSSAR O ("NOME DA IMAGEM", IMAGEM)
cv2.imshow("ABRINDO A IMAGEM", imagem)

# ESPERANDO APERTAR ALGO PARA FECHAR A IMAGEM
cv2.waitKey(0)
