'''
	Colecciones de datos en Python (Tuplas)
	
	Existe cuatro tipos de datos en Python:
	Listas, Tuplas, Sets y Diccionarios
'''

# TUPLAS
# Una tupla es una colección de datos ordenada y NO MODIFICABLE
# Se declaran de la siguiente forma:
estaTupla = ("manzana", "banana", "cereza")
miTuplaNumeros = (1, 9, 4, 2, 5, 8)

# Se accede a los elementos de la misma forma que en las listas
print(estaTupla[1])
print(estaTupla[-1])

# Intervalo
print(miTuplaNumeros[2:5])

# Recorrer en un for
for k in miTuplaNumeros:
  print(k)

# Una vez definida la tupla, esta no puede ser modificada
# por lo que intentar hacer
## estaTupla[1] = "kiwi"
# Producirá un error
# Por lo que, lo que regularmente se hace es utilizar listas
# o realizar conversiones
estaTuplaCopia = list(estaTupla)
estaTuplaCopia[1] = "kiwi"
estaTupla = tuple(estaTuplaCopia)
print(estaTupla)

# Verificar que un elemento exista en la tupla
if "manzana" in estaTupla:
  print("La manzana está en la tupla")

# Solo puede eliminarse por completo la tupla con el operador "del"

# Unir tuplas
tuplaGrande = estaTupla + miTuplaNumeros

# Esto contabiliza cuantas veces aparece un elemento en la tupla
print(tuplaGrande.count('kiwi'))

# Desempaquetar tuplas
elem1, elem2 = (1, "olakease")
print(elem2)
