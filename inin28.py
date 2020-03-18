'''
    INTRODUCCIÓN A LA LIBRERÍA OPENCV DE IMAGENES
    Esta librería permite el manejo y procesamiento de imágenes
    de manera sencilla y eficiente
    Este ejemplo muestra el manejo de las 3 capas de color de una imagen
    Las imágenes RGB se componen de tres canales de color. 
    Una imagen RGB con 8 bits por píxel cuenta con 256 posibles valores para 
    cada canal, lo que significa más de 16 millones de posibles valores 
    de color. En ocasiones, las imágenes RGB con 8 bits por canal se denominan 
    imágenes de 24 bits (8 bits x 3 canales = 24 bits de datos por píxel).
'''
# Descargar la librería openCV
# pip install opencv-python
import cv2
import numpy as np

def nothing(x):
    pass

# Crear una imagen en color negro de tamaño 300x512
# el 3 adicional indica que se trata de una imagen de 3 capas
# esas tres capas son los colores representados como BGR
# Blue Green Red (Azul Verde Rojo) con valores guardados en variables
# de 8 bits sin signo, esto es valores que van de 0 a 255
# 2^8 = 256
img = np.zeros((300,512,3), np.uint8)
# a la imagen se le llama "image"
cv2.namedWindow('image')

# Crear barras para el cambio de color con valores de 0 a 255
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# Crear un switch para funcionalidad ON/OFF
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

while(1):
    cv2.imshow('image',img)
    # Mientras no se presione la tecla ESC, se ejecutará el programa
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    # Obtener las posiciones de las barras
    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    s = cv2.getTrackbarPos(switch,'image')

    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]

cv2.destroyAllWindows()