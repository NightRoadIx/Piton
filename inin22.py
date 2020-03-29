'''
    WEBSCRAPING
    Se trata de leer grandes cantidades de información que se encuentran en
    línea en diversos sitios
    
    Se tiene que considerar lo siguiente:
    1.- Que se puedan utilizar de manera legal estos datos
    2.- No descargar los datos muy rápido, ya que esto "tronaría" el sitio web
        y podría ser bloqueado del sitio
'''
# Se va a hacer análisis del sitio:
# http://web.mta.info/developers/turnstile.html

# Si se hace una inspección del sitio se puede observar los enlaces que contienen
# todos los datos
# <a href=”data/nyct/turnstile/turnstile_180922.txt”>Saturday, September 22, 2018</a>

# Las librerías que se tienen que importar
import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# Grabar el nombre del sitio web
url = 'http://web.mta.info/developers/turnstile.html'
# La respuesta del sitio
response = requests.get(url)
# Ver la respuesta 
print(response)

# Ahora se arreglarán estos datos con una estructura del tipo BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")
# Esto solo muestra el código HTML de la página
print(soup.prettify() )

# Ahora se encontrarán todas las etiquetas <a>
print(soup.findAll('a'))

# No todos las etiquetas nos interesan, pero se puede probar
# OJO, AQUÍ HAY QUE MODIFICAR EL NÚMERO [36], EL CUAL VA VARIANDO YA QUE LOS DATOS SE ACTUALIZAN DIARIAMENTE
one_a_tag = soup.findAll('a')[36]
link = one_a_tag['href']

# Armar la dirección que se va a leer
download_url = 'http://web.mta.info/developers/'+ link
# Se hace la petición para la descarga
urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
# Se detiene el programa por un segundo para evitar problemas
time.sleep(1)

'''
# Ahora solo es cuestión de automatizar para descargar todos los datos del sitio
# Variable para seguir en que línea se encuentra el programa
line_count = 1
for one_a_tag in soup.findAll('a'):
    if line_count >= 36:
        link = one_a_tag['href']
        download_url = 'http://web.mta.info/developers/'+ link
        urllib.request.urlretrieve(download_url,'./'+link[link.find('/turnstile_')+1:])
        time.sleep(1)
    # añadir un 1 para seguir a la otra línea
    line_count += 1
'''
