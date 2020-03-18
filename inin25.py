'''
    DESCARGA DE ARCHIVOS
    Descarga de archivos utilizando la librería urllib
'''
# Usar la librería urllib para descargar archivos
import urllib.request
# Colocar la dirección de lo que se quiere descargar, esto se le conoce como
# URL (Uniform Resource Locator), que indica en donde se encuentran los recursos
# en internet
url = "https://www.python.org/static/img/python-logo@2x.png"
# ESte es el nombre con el que se guardará el archivo
file = "logo.png"
# Hacer un try - except para intentar la descagra
try:
    # En primer lugar se hace la petición para abrir la URL, es en este punto
    # donde puede surgir la excepción
    r = urllib.request.urlopen(url)
    # Una vez que se logra abrir la URL, 
    f = open(file, "wb")
    # Leer lo leído en la URL y escribirlo en el archivo
    f.write(r.read())
    # Recordar super importante, cerrar el archivo
    f.close()
except Exception:
    print("Se ha producido un error")