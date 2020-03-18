'''
    DESCARGA DE VIDEOS DE YOUTUBE
'''
# Instalar la librería pytube
# pip install pytube
# Una vez realizado esto, ya se puede utilizar
from pytube import YouTube 
import os

# Colocar la ruta en donde se salvará
# se obtiene el path en donde se está trabajando o ejecutando el programa
SAVE_PATH = os.getcwd()
  
# Aquí se puede copiar el enlace del video a descargar
link="https://www.youtube.com/watch?v=UnTYOxiaasA"

# ahora se procede a realizar un try - except para controlar excepciones
try: 
    # Generar un objeto YouTube mediante la librería
    # este paso es el que puede generar la excepción
    yt = YouTube(link) 
except: 
    print("Error de conexión")

# Se puede conocer el nombre del video a descargar
print(yt.title)
# y conocer todos los posible formatos a descargar
yt.streams.all()

# supongamos que se desea el primer formato
stream = yt.streams.first()

# Una vez realizado esto, se procede a descargar el video
try: 
    # Descargar el video
    stream.download(SAVE_PATH)
except: 
    print("Error!") 

print('Descarga completa!') 