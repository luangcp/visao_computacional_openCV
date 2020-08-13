"""
Uma das tarefas mais importantes para visão computacional é identificar objetos.
Para essa identificação uma das principais tecnicas é a utilização de detectores de boardas a fim de
identificar os formatos dos objetos presentes na imagem.

Quando falamos em segmentação e detecção de bordas, os algortimos mais comuns são 
o CANDY, SOBEL e variações destes.
Basicamente nestes e em outros metodos a detecção de bordas se faz atraves de identificação do gradiente
ou nesse caso, de variações abruptas na intensidade dos pixels de uma região da imagem;

A openCV disponibiliza a implementação de 3 filtros de gradiente (High-pass filters):
Sobel: cv2.Sobel(), Scharr: cv2.Scharr(), e Laplacian: cv2.Laplacian().
"""
