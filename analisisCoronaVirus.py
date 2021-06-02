# Librería para realizar pedidos por medio de la internet
# Instalar en Anaconda prompt mediante el comando:
# pip install requests
import requests
# con esto para realizar peticiones mediante URL 
# Uniform Resource Locator, Localizador de Recursos Uniforme
# los recursos a los que hace referencia pueden cambiar
import urllib.request
# Para manejo del tiempo
import time
# Manejar páginas web con hipertexto
# Instalar en Anaconda prompt mediante el comando:
# pip install beautifulsoup4
from bs4 import BeautifulSoup

# Manejo de grandes cantidades de datos
import pandas as pd
import numpy as np
import matplotlib.pyplot as mp 


# Esta es la dirección de la página que va a ser analizada
url = 'https://ourworldindata.org/coronavirus/country/united-states'
# Se realizar un pedido a la URL mediante la función get()
respuesta = requests.get(url)
# Estos pedidos puede regresar varios códigos como respuesta, los más comúnes
# son dos:
# 200 -> Recurso localizado
# 404 -> El recurso no fue localizado
print(respuesta)

#%%
# Se halla una página web correcta al obtener el código 200
if respuesta.status_code == 200:
    # Se genera una lista con los posibles enlaces en la página
    listaEnlaces = []
    
    # Se utilizará la librería BeautifulSoup para hallar/obtener la página web
    # solicitada, analizando entonces mediante HTML (el cual es el código con
    # el cual se genera una página web)
    # Hay varios analizadores (lxml, html5lib por mencionar algunos), pero
    # el uso de cada uno dependerá de la aplicación y el grado de análisis que
    # se requiera del código HTML
    sopa = BeautifulSoup(respuesta.text, "html.parser")
    # Con la siguiente instrucción se muestra el código analizado
    print(sopa.prettify())
    # Se comenzará a realizar un análisis del código, al localizar todas las
    # etiquetas <a>, las cuales, en general, hacen referencia a enlaces a otras
    # páginas o recursos
    for enlace in sopa.findAll('a'):
        # el siguiente código a <a> para referirse a un enlace es mediante
        # 'href' (la etiqueta suele ser <a href="recurso">)
        tmp = enlace.get('href')
        # Una vez que se localice esta etiqueta completa, se analiza si cuenta
        # con la cadena "csv", que indica un recurso archivo de valores
        # separados por coma
        if 'csv' in tmp:
            # Se muestra si se encontró uno de estos valores
            print( str(tmp) )
            # Al hallarse se añade a la lista
            listaEnlaces.append(tmp)
            # Se muestra el primer enlace localizado
            # OJO, EN ESTE CASO SABEMOS QUE SÓLO EXISTE UN ENLACE EN ESTA 
            # PÁGINA Y QUE ESTA LLEVA A UN ARCHIVO CSV
            link = listaEnlaces[0]
            
            # Revisar si la lista es no vacía
            if link:
                # Una vez localizada la dirección del recurso donde
                # se almacena el recurso CSV se lee mediante Pandas
                df = pd.read_csv(link)
                
                # Analizar los dato de una locación en particular
                datosMexico =  df[df['location'] == 'Mexico'].fillna(0)
                # Obtener ahora el total de contagios
                TotalContagios = datosMexico['total_cases']
                # Graficar
                mp.plot(TotalContagios)
