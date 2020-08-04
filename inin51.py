#%%
# Las librerÌ≠as que se tienen que importar
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

import pandas
import numpy as np
import matplotlib.pyplot as mp

#%%
# DESCARGA DE DATOS
# Grabar el nombre del sitio web
url = 'http://web.mta.info/developers/turnstile.html'
# La respuesta del sitio
response = requests.get(url)
# Ver la respuesta 
print(response)

#%%
# Ahora se arreglar·n estos datos con una estructura del tipo BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# Esto solo muestra el cÛdigo HTML de la p·gina
print(soup.prettify() )

#%%
# Ahora se encontrar·n todas las etiquetas <a>
print(soup.findAll('a'))

# No todos las etiquetas nos interesan, pero se puede probar
# OJO, AQUÕç HAY QUE MODIFICAR EL N⁄MERO, EL CUAL VA VARIANDO YA QUE LOS DATOS SE ACTUALIZAN DIARIAMENTE
one_a_tag = soup.findAll('a')[43]
link = one_a_tag['href']

#%%
# Armar la direcciÛn que se va a leer
download_url = 'http://web.mta.info/developers/'+ link
# Se hace la peticiÛn para la descarga
urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
# Se detiene el programa por un segundo para evitar problemas
time.sleep(1)

#%%
# OBTENCI”N DE DATOS

# Obtener el nombre del archivo
archon = link.split("/")[-1]

# Apertura del archivo usando PANDAS
df = pandas.read_csv(archon)

#%%
# Obtener una lista de todas las estaciones
# df["STATION"].unique().tolist()

# Analizar los datos de una sola estaciÛn
estacion = df[df["STATION"] == "59 ST"]

# Obtener solo un valor de SCP de los datos de dicha estaciÛn
scpfinal = estacion[estacion["SCP"] == "02-00-00"]


#%%
# Obtener los valores ˙nicos de las fechas
fechas = scpfinal["DATE"].unique().tolist()

# fechas[0]
for f in fechas:
    mp.plot( scpfinal[scpfinal["DATE"] == f]["TIME"].tolist(), 
        scpfinal[scpfinal["DATE"] == f]["ENTRIES"].tolist() )

mp.title("Entries for the station " + scpfinal["STATION"].unique().tolist()[0] + 
         "using SCP = " + scpfinal["SCP"].unique().tolist()[0] )
mp.grid()
mp.xlabel("TIME")
mp.ylabel("ENTRIES")
mp.legend(fechas, loc = 'upper right')
mp.show()
