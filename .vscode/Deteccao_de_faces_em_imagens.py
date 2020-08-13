"""
Busca-se desenvolver a habilidade de identificar padrões de imagem através de visão computacional
e varias tecnicas foram criadas nos ultimos anos visando esse objetivo

Atualmente o que há de mais moderno são as tecnicas de deep learning -> aprendizado profundo de maquina.
Que envolvem algoritmos de inteligência artificial e redes neurais para treinar identificadores

Outra tecnica bastante utilizada e MUITO importante são os haae cascades -> caracteriticas em cascata do tipo haar
A principal vantagem tecnica é a baixa necessidade de processamento para realizar a identificação dos objetos, o que
o que se traduz em alta velocidade de detecção

Os argumentos que precisam ser informados para o metodo de detecção além do arquivo xml 
que contem a descrição do objeto são:

ScaleFactor: Quando o tamanho da imagem é reduzido em cada busca da imagem. 
Isso é necessario porque podem ter objetos grandes (próximos) ou manores (mais distantes) na imagem.
Um valor de 1,0 indica que a imagem sera reduzinha em 5% cada vez

minNeighbors: Quantos vizinhos cada janela deve ter para a area da janela ser considerada um rosto. O classificador
em cascata detectara varias janelas ao redor da face e este parametro controla quantas janelas positivas são
necessarias para se considerar um rosto valido

minSize: Uma tupla de largura e altura (em pixels) indicando o tamanho minimo da janela para que caixas menores
do que este tamanho serão ignoradas
"""
# INDENTIFICANDO FACES
# IMPORTANDO BIBLIOTECAS
import cv2
import numpy as np
import imutils
import mahotas
from matplotlib import pyplot

# CARREGANDO ARQUIVO E CONVERTENDO PARA TONS DE CINZA
imagem = cv2.imread('imagem/variaspessoas.png')
imagem_preta_e_branca = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

# Criando detector de faces
detector = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')

# Executando a detecção
faces = detector.detectMultiScale(imagem_preta_e_branca,
                                  scaleFactor=1.05, minNeighbors=7, minSize=(30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

# DESENHANDO RETANGULOS SOBRE AS FACES
for (x, y, w, h) in faces:
    cv2.rectangle(imagem, (x, y), (x + w, y + h), (0, 255, 255), 7)

# Exibindo a imagem
cv2.imshow(str(len(faces))+' Rostos encontrados', imagem)
# Espera apertar algo pra sair
cv2.waitKey(0)
