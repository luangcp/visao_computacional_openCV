"""
Outra tecnica muito util é a de escrever sobre imagem. Para isso lembre-se que a 
coordenada do texto refere-se a base onde os caracteres começaram a ser escritas.
Então para um calculo preciso estude a função 'getTextSize'. O exemplo abaixo tem 
o resultado a seguir:
"""
# Importando bibliotecas
import cv2
import numpy as np
import imutils

# Lendo as imagens
imagem = cv2.imread('imagem/ponte.jpg')

# DEFININDO A FONTE
fonte = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagem, 'OpenCV', (15, 65), fonte,
            2, (255, 255, 255), 2, cv2.LINE_AA)

# Abrindo a imagem
cv2.imshow('Imgagem com texto', imagem)
# Esperando apertar algo pra sair
cv2.waitKey(0)
