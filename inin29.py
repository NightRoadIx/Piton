# Cargar la libreria numpy como np
import numpy as np
# Importar cv2 (la libreria del opencv)
import cv2

# Leer una imagen, el 0 indica que en color gris
# Para este caso se usa una imagen JPG (modificar image.jpg, dicha imagen debe estar en la misma
# carpeta que el scrpit de Python o se debe indicar la dirección completa del archivo)
img = cv2.imread('imagen.jpg',1)
# El segundo argumento es una bandera la cual especifíca el camino en la que la imagen será leída.
# cv2.IMREAD_COLOR : Carga una imagen a color. Cualquier transparencia de imagen será omitida. Es la opción por defecto. 1
# cv2.IMREAD_GRAYSCALE : Carga una imagen en escala de grises. 0
# cv2.IMREAD_UNCHANGED : Carga una imagen en la que se incluye el canal alpha (transparencia). -1

# el canal alfa es un componente de color que representa el grado de transparencia (u opacidad) de un color
# esto es, los canales de color RGB. Es utilizado para determinar como un pixel esta renderizado cuando se mezcla con otro
# usado cuando una imagen se sobrepone a otra

# Abrir una ventana con la imagen
cv2.imshow('image',img)
# Esperar una tecla y recibirla en la variable
k = cv2.waitKey(0)
if k == 27:				# Tecla ESC
	# Finalizar la ventana
    cv2.destroyAllWindows()
elif k == ord('s'):		# Tecla 's'
	# Reescribir la ventana
    cv2.imwrite('endgame.png',img)
    cv2.destroyAllWindows()

