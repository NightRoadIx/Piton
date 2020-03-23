'''
    GENERACIÓN DE UN FRACTAL CON PYTHON
    Este código permite crear un fractal Mandelbrot
    Dicho fractal es un conjunto de números complejos c para cuya función
    f(z) = z**2 + c no diverge cuando es iterada desde z = 0.
    Este se trata de uno de los fractales más conocidos
    
    Se requiere tener instaladas las librerías:
        PIL
        numpy
        colorsys
'''
# Mandar a llamar las librerías
# Python Image Library
from PIL import Image 
from numpy import complex, array 
import colorsys 
  
# Aquí se coloca el tamaño (anchura) de la imagen a generar
WIDTH = 1024
  
# Esta función regresa una tupla de valores RGB
def rgb_conv(i):
    # Recordar que los valores de los colores van de 0 a 255 al tratarse
    # de una variable unsigned int de 8 bits
    color = 255 * array(colorsys.hsv_to_rgb(i / 255.0, 1.0, 0.5)) 
    return tuple(color.astype(int)) 
  
# La función que define al fractal
def mandelbrot(x, y): 
    # Crear un número complejo a partir de los parámetros (x,y)
    c0 = complex(x, y)
    c = 0
    # Para valores de 1 a 1000
    for i in range(1, 1000):
        # Si |c| > 2
        if abs(c) > 2:
            # Se regresa el valor en RGB de i
            return rgb_conv(i)
        # Esta es la función Mandelbrot
        c = c * c + c0
    # Terminar regresando una tupla
    return (0, 0, 0) 
  
# Dentro de la librería PIL se encuentra el crear una imagen
# en formato RGB de tamaño ancho, ancho/2
img = Image.new('RGB', (WIDTH, int(WIDTH / 2))) 
# Cargar la imagen en una variable
pixels = img.load() 

for x in range(img.size[0]): 
    # Mostrar el progreso de la generación del fractal
    print("%.2f %%" % (x / WIDTH * 100.0))  
    # Se arma el fractal
    for y in range(img.size[1]): 
        pixels[x, y] = mandelbrot((x - (0.75 * WIDTH)) / (WIDTH / 4), 
                                      (y - (WIDTH / 4)) / (WIDTH / 4)) 
  
# Finalmente desplegar la imagen generada
img.show() 