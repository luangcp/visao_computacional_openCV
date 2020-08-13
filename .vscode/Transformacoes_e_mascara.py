""" Em muitas ocasiões é necessario realizar transformações sobre a imagem. Ações como redimensionar
cortar ou rotacionar uma imagem são necessariamente frequentes. Esse processamento pode ser feito
de farias formar
"""

""" Cortando uma imagem/crop.
A mesma tecnica já usada para fazer slicing pode ser usada para criar uma nova imagem recortada
da imagem original, o termo em inglês é crop. Veja o codigo abaixo onde criamos uma nova imagem a partir de um pedaço
da imagem original e a salvamos no disco """

# Importando bibliotecas

# Lendo a imagem
import cv2
import numpy as np
import imutils
imagem = cv2.imread('imagem/ponte.jpg')

# Recortando
recorte = imagem[100:200, 100:200]

# Abrindo a imagem
cv2.imshow('Recorte de imagem', recorte)
# Salvando a imagem
cv2.imwrite('Recorte.jpg', recorte)
# Esperando apertar algo para fechar
cv2.waitKey(0)
