"""
IDENTIFICANDO E CONTANDO OBJETOS

Exemplo de contagem de dados:
Jogar os dados e o computador ira ver sua pontuação

Para isso precisamos identificar:
1 - Onde estão os dados na imagem
2 - Quantos dados foram jogados
3 - Qual é o lado que esta para cima

Inicialmente vamos identificar os dados e contar quantos dados existem na imagem
em um segundo momento iremos identificar quais são esses dados. 

PASSO A PASSO:
1 - Converter a imagem para tons de cinza
2 - Aplicamos bur para retirar o ruido e facilitar a identificação das bordas.
3 - Aplicamos uma binarização na imagem resultando em pixels só brancos e pretos
4 - Aplicamos um detector de bordar pasa identificar os objetos 
5 - Com as bordas identificadas, vamos contar os contornos externos para achar a quantidade de dados
presentes na imagem
"""
# Importando bibliotecas
import cv2
import numpy as np
import mahotas


# FUNÇÃO PARA FACILITAR A ESCRITA NAS IMAGENS


def escreve(imagem, texto, cor=(255, 0, 0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(imagem, texto, (10, 20), fonte, 0.5, cor, 0, cv2.LINE_AA)


# Lendo a imagem
imagem_colorida = cv2.imread('imagem/dados.jpg')

# Passo 1 -> CONVERTENDO PARA TONS DE CINZA
imagem = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

# Passo 2 -> SUAVIZANDO A IMAGEM COM BLUR
suave = cv2.blur(imagem, (7, 7))


# Passo 3 -> Binarização resultando em pixels brancos e pretos
T = mahotas.thresholding.otsu(suave)
bin = suave.copy()
bin[bin > T] = 255
bin[bin < 255] = 0
bin = cv2.bitwise_not(bin)

# Passo 4 -> Detecção de bordas com Canny
bordas = cv2.Canny(bin, 70, 150)

# Passo 5 -> Identificação e contagem dos contornos da imagem
# cv2.RER_EXTERNAL = CONTA APENAS OS CONTORNOS EXTERNOS
(lx, objetos, lx) = cv2.findContours(
    bordas.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# a VARIVAEL lx (lixo), recebe dados não utilizaos

escreve(imagem, "Imagens em tons de cinza", 0)
escrece(suave, "suavização com Blur", 0)
escreve(bin, "binarização com metodo Otsu", 255)
escreve(bordas, "detector de bordas Canny", 255)

# TUDO EM UMA IMAGEM
resultado = np.vstack([
    np.hstack([imagem, suave]),
    np.hstack([bin, bordas])
])

cv2.imshow("Quantidade de objetos:"+str(len(objetos)), resultado)
cv2.waitKey(0)

imagemC2 = imagem_colorida.copy()
cv2.imshow('Imagem Original', imagem_colorida)

cv2.drawContours(imagemC2, objetos, -1, (255, 0, 0), 2)

escreve(imagemC2, str(len(objetos))+"Objetos encontrados!")

cv2.imshow("Resultado", imagemC2)
cv2.waitKey(0)
