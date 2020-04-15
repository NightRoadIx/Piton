# Importar la librería request
import requests
import numpy as np
import matplotlib.pyplot as plt
import random

# De request lo que se hace es usar el método get para obtener algún archivo que este en línea
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
# Con esto se muestra el resultado
type(res)
# En caso de que se haya localizado el archivo se coloca el código de estátus como OK
res.status_code == requests.codes.ok
# Obtener la longitud del texto leído
len(res.text)
# Mostrar todo el texto
print(res.text[:250])

# Ahora hacer la contabilidad de las letras
# Crear la lista con las letras
testList = [chr(x) for x in range(ord('a'), ord('z') + 1) ]
# Crear el número de ocurrencias
ocurrenc = [0] * len(testList)

# Contar la ocurrencia de cada letra
i = 0
for k in testList:
    ocurrenc[i] = res.text.count(k)
    i += 1

# Armar un diccionario con las letras y sus ocurencias
zipObj = zip(testList, ocurrenc)
dicLetras = dict(zipObj)

# Marcar que se utilizará un estilo con fondo oscuro
plt.style.use("dark_background")
# Graficar la ocurrencia de cada letra
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
barras = ax.bar(testList, ocurrenc)
ax.set_xlabel('Letras')
ax.set_ylabel('# de Ocurrencias')
for i in range(len(testList)):
    barras[i].set_color((random.random(), random.random(), random.random()))
plt.show()
