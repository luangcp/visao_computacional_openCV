"""
ABAIXO TEMOS UM CODIGO COMPLETO COM VARREDURA DE DIRETORIO, OU SEJA: é possivel repassar 
um diretorio para busca e o algoritmo irá procurar por todas as imagens do diretorio,
identificar as faces e criar um retangulo sobre as faces encontradas

"""
# Importando bibliotecas
import os
import cv2

# FAZ A VARREDURA DO DIRETORIO IMAGEM BUSCANDO ARQUIVOS JPG, JPEG E PNG
diretorio = 'imagem'
arquivos = os.listdir(diretorio)

# Iniciando loop de varredura
for a in arquivos:
    if a.lower().endswith('.jpg') or a.lower().endswith('.png') or a.lower().endswith('.jpeg'):
        imagem_colorida = cv2.imread(diretorio+'/'+a)
        imagem_peb = cv2.cvtColor(imagem_colorida, cv2.COLOR_BGR2GRAY)

        df = cv2.CascadeClassifier(
            'cascade/haarcascade_frontalface_default.xml')
        faces = df.detectMultiScale(imagem_peb, scaleFactor=1.2, minNeighbors=7, minSize=(
            30, 30), flags=cv2.CASCADE_SCALE_IMAGE)

        for (x, y, w, h) in faces:
            cv2.rectangle(imagem_colorida, (x, y),
                          (x+w, y+h), (0, 255, 255), 7)

            alt = int(imagem_colorida.shape[0]/imagem_colorida.shape[1]*640)
            imagem_colorida = cv2.resize(
                imagem_colorida, (640, alt), interpolation=cv2.INTER_CUBIC)

            cv2.imshow(str(len(faces))+' Rostos encontrados', imagem_colorida)
            cv2.waitKey(0)
