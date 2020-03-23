'''
    Generar códigos QR con Python
    se requiere instalar las librerías
    pip install pyqrcode
    pip install pypng
'''
# Importar pyqrcode
import pyqrcode
# ir directo a la librería que se va a a utlizar
from pyqrcode import QRCode 
  
# Esta es la cadena que representará al código QR
s = "http://verikosesi.rf.gd/index.html"
  
# Generar el código QR
url = pyqrcode.create(s) 
  
# Se salva la imagen con formato PGN llamada "micodigoqr.png", en una escala 
# x8 (esto aumenta el tamaño de la imagen)
url.png("micode.png", scale=8)