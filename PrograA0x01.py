#%%
# from LIBRERIA import * (TOCHO MOROCHO)
from sympy import *
# Desempacando un set en varias variables
# (esto viola uno de los principios de la programación funcional)
# y = f(x,w,t,r,...)
x, y, z = symbols('x y z')
init_printing()

Integral(sqrt(1/x), x)

#%%
# Vamos a mandar a llamar una librería
# import LIBRERIA as NOMBRE
import pandas as pd

# Leer un archivo CSV
# DataFrame = pandas.read_csv('RUTA/ARCHIVO.CSV')
# RUTA => (local) C:/Mis Documentos/...
#      => (internet) http://www....
df = pd.read_csv('https://covid.ourworldindata.org/data/owid-covid-data.csv')

#%%
# Ver la tabla de datos, primeras y últimas 5 filas
df

#%%
# df => Objeto tabla de datos
# Observar las primeras n filas (n = 5 por defecto)
df.head(6)

#%%
# Observar las últimas n filas (n = 5 por defecto)
df.tail(10)

#%%
# Obtener la información de los datos del DatFrame
df.info()

#%%
# Estadística básica de todo el DataFrame
df.describe()

#%%
# revisar los primeros 20 datos de la columna 'continent'
df['continent'].head(20)

#%%
# Obtener un DataFrame con booleanos donde se cumpla esta condición
df['continent'] == 'Europe'

#%%
# Obtener una DataFrame con datos en particular de la columna 'continent'
df[df['continent'] == 'Europe']