"""
A suavisação da imagem (do inglês Smoothing), também chamada de 'blur' ou 'blurring' que podemos traduzir
para borrão, é um efeito que podemos notas nas fotografias fora de foco ou desfocadas onde tudo fica embasado.

Esse efeito na verdade pode ser criado digitalmente, basta alterar a cor de cada pixel misturando a cor
com os pixells ao seu redor. Esse efeito é muito util quando utilizamos algoritmos de identificação de objetos
em imagens pois os processos de detecção de bordar por exemplo, funconam melhor dps de suavizar a imagem.
"""

"""
SUAVIZAÇÃO POR CÁLCULO DA MÉDIA:
    Nesse caso é criada uma caixa de pixels para envolver o pixel em questão e calcular seu novo valor.
    O novo valor do pixel será a media simples dos valores dos pixels dentro da caixa, ou seja, dos pixels 
    da vizinhança. Alguns autores chamam esta caixa de janela de cálculo ou kernel(nucleo).
"""

"""
No codigo abaixo percebemos que o metodo utilizado para a suavização pela média é o método 'BLUR' da OpenCV
Os parametros são a imagem a ser suavizada e a janela de suavização. Colocarmos números impars para gerar as
caixas de calculo pois dessa forma não existe duvida sobre onde estará o pixel central que terá seu valor atualizado

Usamos as funções vstack (pilha vertical) e hstack (pilha horizontal) para juntar as imagens em uma unica imagem final
mostrando desde a imagem original e seguinte com caixas de calculo de 3x3, 5x5, 9x9, e 11x11.
Conforme a caixa aumenta maior é o efeito do borrão (blur) na imagem
"""

# Importano as bibliotecas

# Lendo a imagem
import cv2
import numpy as np
import imutils
from matplotlib import pyplot as plt
imagem = cv2.imread('imagem/ponte.jpg')

# Diminuindo a imagem
imagem = imagem[::2, ::2]

# Função utilizada para juntar todas as imagens em uma só
suave = np.vstack([
    np.hstack([imagem, cv2.blur(imagem, (3, 3))]),
    np.hstack([cv2.blur(imagem, (5, 5)), cv2.blur(imagem, (7, 7))]),
    np.hstack([cv2.blur(imagem, (9, 9)), cv2.blur(imagem, (11, 11))]),
])

# Abrindo as imagens suavizadas Blur
cv2.imshow('Imagens suavizadas (Blur)', suave)
# Esperando apertar algo para fechar
cv2.waitKey(0)
