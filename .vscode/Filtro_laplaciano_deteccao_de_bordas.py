""" O filtro laplaciano não exige processamento individual
horizontal e vertical como o Sobel. Um unico passo é
necessario para gerar a imagem. Contudo, também é
necessario trabalhar com a representação do pixel
em um ponto flutuante de 64bits com sinal para
depois converter novamene para inteiro sem
sinal de 8 bits """
# Importando bibliotecas
import cv2
import numpy as np

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Convertando para preto e brando
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Metodo laplacian
lap = cv2.Laplacian(imagem, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))

# Tudo numa mesma imagem
resultado = np.vstack([imagem, lap])

# Criando a imagem
cv2.imshow('Filtro laplaciano', resultado)

# Esperando apertar algo para fechar
cv2.waitKey(0)
