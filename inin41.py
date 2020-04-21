'''
    Captura de fotogramas a partir de una cámara web
    Este programa permite obtener una imagen de una cámara web
    conectada a la computadora
'''
# Integrar las librerías numpy y opencv
import numpy as np
import cv2

# Utilizar la función de opencv VideoCapture(0)
# donde 0 es el número de la cámara web conectada a la computadora
cap = cv2.VideoCapture(0)

# Con este ciclo se tomarán múltiples imágenes, simulando el video
while(True):
    # Capturar cuadro por cuadro
    # La función read() regresa dos valores
    # ret   : Regresa si la cámara obtuvo un fotograma
    # frame : El fotograma (la fotografía) tomada
    ret, frame = cap.read()

    # --Las operaciones que se hacen en el frame--
    # En este caso se hace que lo capturado este en escala de grises
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Mostrar el frame resultante
    cv2.imshow('frame',gray)
    # La salida o el fin del ciclo, es mediante la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Una vez hecho todo, se tiene que liberar la captura de datos
cap.release()
cv2.destroyAllWindows()
