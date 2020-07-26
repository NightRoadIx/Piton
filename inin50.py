'''
    Librería pandas para el manejo de grandes cantidades de información
    Esta librería permite realizar análisis de información en archivos CSV
    principalmente (Comma Separated Values).
    
    pip install pandas
    
    Más información de la librería pandas:
        https://pandas.pydata.org/docs/getting_started/index.html
'''
# Importar la librería
import pandas

# Leer los datos de un archivo
# el parámetro index_col = 0, indica que la columna 0 funcionará como el índice
# df = pandas.read_csv('nba.csv', index_col = 0)
df = pandas.read_csv('nba.csv')

# Ver algunos de los datos leídos (los primeros y últimos)
print(df)

# Tamaño de los datos
df.shape

# Mostrar solo los primeros 5 registros (este número puede cambiar al colocar
# como argumento a .head(n) el número n de datos)
print(df.head())

# Ahora mostrar los últimos 5 datos
print(df.tail())

# Tipos de datos
print(df.dtypes)

# información de los datos
print(df.info())

# ver la estadística de los datos
# conteo, promedio, desviación estándar, mínimo, máximo y cuartiles
print(df.describe())

# Se puede analizar columna de manera individual
df["Age"]

# Conocer las propiedades estadísticas de los datos de una columna en particular
df["Age"].mean()

# O de más de una columna
df[["Age", "Weight"]].median()

# Contabilizar el número de datos
df["Age"].value_counts()

# graficar todos los datos
df.plot()

# graficar en específico algún dato
df["Salary"].plot()

# Graficar en específico
df.plot.scatter(x = "Age", y = "Salary", alpha = 0.5)

# Obtener solo datos en específico de una tabla, para crear otra
nueva = df[["Name", "Team", "Number", "Position"]]

# Obtener datos específicos de filas
jazz = df[df["Team"] == "Utah Jazz"]

# # # # # # # #
# Gradicar datos con Matplotlib
import matplotlib.pyplot as mp

# Se convierten los datos a lista
x = df["Height"].tolist()
y = df["Salary"].tolist()

mp.plot(x, y, 'r.')
