""" A diferença da equalização também é vizivel na imagem, contudo, conforme vemos na imagem é possivel
que ocorram distorções e alterações nas cores da imagem equalizada, portando, nem sempre a imagem
mantem suas caracteristicas originais. Caso exista a necessidade de destacar detalhes na imagem
a eqaulização pode ser uma grande aliada. NORMALMENTE É FEITO EM IMAGENS PARA A IDENTIFICAÇÃO 
DE OBJETOS, IMAGENS DE ESTUDOS DE ÁREAS POR SATELITE E PARA IDENTIFICAÇÃO DE PADRÕES EM IMAGENS
MEDICAS.

o calculo matematico da equalização do histograma da imagem é feito pela função 'equalizeHist'
disponibilizada pela OpenCV.

A equalização faz com que a distribuição das intensidades dos pixels de 0 a 255 seja uniforme.
Portanto teremos a mesma quantidade de pixels com valores na faixa e 0 a 10 (pixels muto escuros)
e na faixa de 245 a 255 (pixels muito claros).

Funciona da seguinte maneira:

Passo 1: Calcula o historama 'H' da imagem;
Passo 2: Normaliza o histograma para garantir que os valores das intensidades 
dos pixels estejam entre 0 e 255.
Passo 3: Calcula o histograma acumulado
Passo 4: Transforma a imagem
"""
