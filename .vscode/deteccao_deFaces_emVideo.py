"""
O processo de detecção de objetos em videos é muito similar a detecção em imagens
Na verdade em video nada mais é do que um fluxo continuo de imagens que são enviadas a partir da fonte
como uma webcam ou video mp4

Um looping é necessario para processar o fluxo continuo de imagen do video. 
Para facilitar a compreenção:
"""
# Importando bibliotecas
import cv2

# Função para redimensionar uma imagem


def redim(imagem, largura):
    alt = int(imagem.shape[0]/imagem.shape[1]*largura)
    imagem = cv2.resize(imagem, (largura, alt), interpolation=cv2.INTER_AREA)
    return imagem


# Criando detector de faces baseados no XML
df = cv2.CascadeClassifier('cascade/haarcascade_frontalface_default.xml')

# Abre um video gravado em disco
camera = cv2.VideoCapture('videos/detectandorosto.mp4')

while True:
    # read() retorna 1- Se houver sucesso e 2- O propio frame
    (sucesso, frame) = camera.read()
    if not sucesso:
        break

    # Reduz o tamanho do frame para acelerar o processamento
    frame = redim(frame, 320)
    # Convertendo para tons de cinza
    frame_peb = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detectando as faces no frame
    faces = df.detectMultiScale(frame_peb, scaleFactor=1.1, minNeighbors=3, minSize=(
        20, 20), flags=cv2.CASCADE_SCALE_IMAGE)
    frame_temp = frame.copy()

    for (x, y, lar, alt) in faces:
        cv2.rectangle(frame_temp, (x, y),
                      (x + lar, y + alt), (0, 255, 255,), 2)

        # Exibe um frame redimensionado (com perca de qualidade)
        cv2.imshow('Encontrando rostos..', redim(frame_temp, 640))

        # Espera que aperte S para sair
        if cv2.waitKey(1) & 0xFF == ord('s'):
            break

# FECHANDO STREAMING
camera.release()
cv2.destroyAllWindows
