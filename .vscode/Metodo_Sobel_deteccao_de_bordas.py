"""
Não encontraremos na explicação matematica de cada metodo mas
é importante notar que o Sobel é direcional, então temos que
juntar o filtro horizontale o vertical para teruma transformação completa
"""
# Importando bibliotecas
import cv2
import numpy as np
# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Convertendo para preto e branco
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Metodo sobel
sobelX = cv2.Sobel(imagem, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(imagem, cv2.CV_64F, 0, 1)
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))
sobel = cv2.bitwise_or(sobelX, sobelY)

# Colocando tudo numa mesma imagem
resultado = np.vstack([
    np.hstack([imagem, sobelX]),
    np.hstack([sobelY, sobel])
])

# Abrindo a imagem
cv2.imshow('Sobel', resultado)
# Esperando apertar algo para fechar
cv2.waitKey(0)

"""
Note que devido ao processamento do Sobel é preciso trabalhar com a imagem
com ponto flutuante de 64 bits( que suporta valores positivos e negativos) para
depois converter para uint8 novamente.
"""
