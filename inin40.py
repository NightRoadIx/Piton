'''
    SELENIUM
    Es una librería para hacer pruebas en paginas web
    
    pip install selenium
    pip install webdriver-manager


    Más información
    https://selenium-python.readthedocs.io/installation.html
'''
# Importar la librería selenium el webdriver
from selenium import webdriver
# Para el manejo con Chrome, aunque se puede realizar con otros navegadores
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys

# Instalar el driver del Chrome puesto que no siempre al instalarse en 
# el sistema, Chrome permite "lanzar" o ejecutar la aplicación desde cualquier
# punto, con esto se hace referencia a que Chrome se instala en el PATH del 
# sistema, el cual, al acceder al Símbolo del Sistema (cmd) pueda ejecutar
# Chrome con solo escribir el nombre del ejecutable chrome.exe
# para más información del PATH del sistema, se puede revisar en las siguientes
# páginas web:
# https://es.wikipedia.org/wiki/PATH_(inform%C3%A1tica)
# https://www.softzone.es/windows-10/como-se-hace/cambiar-path-variables-entorno/
# http://chuwiki.chuidiang.org/index.php?title=Path_de_ejecutables_en_Windows
driver = webdriver.Chrome(ChromeDriverManager().install())

# Maximizar la ventana cuando se mande a llamar
driver.maximize_window()
# Hacer una llamada al navegador e ingresar a la página
driver.get("https://www.google.com")

# Colocar en la caja de búsqueda el siguiente letrero
# esto se puede buscar con ingresar al inspector de elementos en Chrome
elem = driver.find_element_by_name("q")
# Limpiar lo que este escrito
elem.clear()
# Enviar el siguiente texto
elem.send_keys("Koreanovirooo")
# y la siguiente tecla
elem.send_keys(Keys.ENTER)

# "Dormir" el proceso unos 3 segundos
time.sleep(3)  

# Cerrar el driver y la ventana
driver.close()