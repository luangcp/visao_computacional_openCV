"""
Thresholding pode ser traduzido por limiarização e no caso de processamento de imagens na maior parte
das vezes utilizamos para binarização da imagem. Normalmente convertemos imagens em tons de cinza para imagens
preto e branco onde todos os pixels possuam 0 ou 255 como valores de intensidade

EM CASO DE ESTRADAS ESTA É UMA DAS TECNICAS UTILIZADAS POR CARROS AUTÔNOMOS PARA IDENTIFICAR A PISTA
A MESMA TÉCNICA TAMBÉM É UTILIZADA PARA IDENTIFICAÇÃO DE OBJETOS
"""
# Importando bibliotecas
import cv2
import imutils
import numpy as np
from matplotlib import pyplot as plt

# Lendo a imagem
imagem = cv2.imread('imagem/ponte.jpg')

# Convertendo a imagem para preto e branco
imagem = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Suavizando a imagem com GaussianBlur
suave = cv2.GaussianBlur(imagem, (7, 7), 0)  # APLICA BLUR

(T, bin) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY)

(T, binI) = cv2.threshold(suave, 160, 255, cv2.THRESH_BINARY_INV)

resultado = np.vstack([
    np.hstack([suave, bin]),
    np.hstack([binI, cv2.bitwise_and(imagem, imagem, mask=binI)])
])

# Abrindo a imagem
cv2.imshow('Binarização da imagem', resultado)

# Esperando apertar algo para fechar
cv2.waitKey(0)

"""
NO CODIGO REALIZAMOS A SUAVIZAÇÃO DA IMAGEM, O PROCESSO DE BINARIZAÇÃO COM THRESHOLD DE 160 E A INVERSÃO
DA IMAGEM BINARIZADA
"""

"""
RESULTADO FINAL: Imagem, imagem suavizada, imagem binarizada e binarizada invertida.
"""
"""
EM CASO DE ESTRADAS ESTA É UMA DAS TECNICAS UTILIZADAS POR CARROS AUTÔNOMOS PARA IDENTIFICAR A PISTA
A MESMA TÉCNICA TAMBÉM É UTILIZADA PARA IDENTIFICAÇÃO DE OBJETOS
"""
