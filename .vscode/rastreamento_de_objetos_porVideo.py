"""
O rastreamento de objetos é muito util em aplicações reais. Realizar o rastreamento envolve identificar um objeto
e apos isso acompahar em sua trajetoria. Uma das maneiras para identifica um objeto é utilizar a tecnica das caracteristicas
hear like. Outra maneira ainda mais simples é simplesmente definir uma cor especifica para rastrear um objeto.

O objetivo do codigo abaixo é identificar e acompanhar um objeto azul na tela. Perceba que o a cor azul
pode ter varias tonalidades e é por isso que a função cv2.inRange() é tão importante. Essa função recebe uma cor azul-claro
e outra azul-escuro e tudo que estiver entre essas duas tonalidades será identificado como sendo parte 
de nosso objeto. A função retorna uma imagem binarizada.
"""
# Importando bibliotecas
import numpy as np
import cv2
import imutils

# Definindo as cores
azul_escuro = np.array([100, 67, 0], dtype='uint8')
azul_claro = np.array([255, 128, 50], dtype='uint8')

# camera = cv2.VideoCapture(args["video"]
camera = cv2.VideoCapture('videos/race.mp4')

while True:
    (sucesso, frame) = camera.read()
    if not sucesso:
        break
    obj = cv2.inRange(frame, azul_escuro, azul_claro)
    obj = cv2.GaussianBlur(obj, (3, 3), 0)
    cnts, _ = cv2.findContours(obj.copy(),
                               cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(cnts) > 0:
        cnt = sorted(cnts, key=cv2.contourArea, reverse=True)[0]
        rect = np.int32(cv2.boxPoints(cv2.minAreaRect(cnt)))
        cv2.drawContours(frame, [rect], -1, (0, 255, 255), 2)

    cv2.imshow('Tracking', frame)
    cv2.imshow('Binary', obj)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
