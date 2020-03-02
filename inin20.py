# Importar el módulo para la conversión de texto a audio
# Utilizar desde el prompt de Anaconda el comando:
# pip install gTTS
# para instalar la librería y comenzar a utilizarla
from gtts import gTTS 

# se importa este módulo para poder ejecutar el auido convertido
import os 
  
# El texto que se desea convertir en audio
mytext = 'All host station primary defenses and weapons systems are online!'
  
# El lenguaje al que se desea convertir, una lista de los lenguajes disponibles
# se puede obtener al ejecutar el comando:
# gtts-cli --all
# en el prompt de Anaconda
language = 'en'
  
# Pasar el texto y el lenguaje al motor, además se utiliza o marca
# slow=False, lo cual le dice al móduo que el texto convertido en audio
# será reproducido en alta velocidad
myobj = gTTS(text=mytext, lang=language, slow=False) 
  
# Salvar el audio en un archivo mp3
myobj.save("welcome.mp3") 
  
# Reproducir el archivo generado
os.system("start welcome.mp3") 


#%%
'''
    Para reproducir el texto directamente se puede utilizar lo siguiente
    Instalar:
        pip install gTTS
        pip install SpeechRecognition
        pip install playsound
'''
import speech_recognition as sr
from gtts import gTTS
import os
import time
import playsound

def speak(text, lan):
    tts = gTTS(text=text, lang=lan)
    filename = 'voice.mp3'
    tts.save(filename)
    playsound.playsound(filename)

speak("Eu acho que o reconhecimento de voz é uma tarefa difícil", "pt")