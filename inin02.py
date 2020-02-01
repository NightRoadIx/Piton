'''
	Colecciones de datos en Python (Arreglos)
	
	Existe cuatro tipos de datos en Python:
	Listas, Tuplas, Sets y Diccionarios
'''

# LISTAS
# Una lista es una colección de datos ordenada y cambiable
# Se declaran de la siguiente forma:
miLista = ["manzana", "banana", "cereza"]
miListaNumeros = [1, 9, 4, 2, 5, 8]

# Para acceder a los elementos de la lista
print(miLista[1])
# El índice de la lista inicia en 0

# ... sin embargo también existe los siguiente
print(miLista[-1])
# Es posible utilizar un indexado negativo para acceder
# a los elementos de la lista

# O también acceder a un rango de datos (generar una sublista)
print(miListaNumeros[2:5]) # en el intervalo [2, 5)
# puede dejarse en blanco alguno de los números
# iniciar desde el el primer elemento (miLista[:n])
# o de un cierto índice al final (miLista[n:])

# Cambiar valores
miLista[1] = "lychee"

# Recorrer una lista
for k in miListaNumeros:
  print(k)

# Determinar la longitud de una lista
print("Longitud de la lista " + str(len(miListaNumeros)))

# Añadir elementos a la lista
miLista.append("naranja")
print(miLista)

# Añadir en algún lugar en particular, recorriendo
# los elementos para dar espacio
miLista.insert(1, "banana")

# Eliminar un elemento en particular
miLista.remove("banana")

# O también mediante la función pop() y el índice del elemento
miLista.pop(1)

# El método clear(), limpia la lista de elementos
miLista.clear()

# La función del elimina las variables
# del miLista

# Copiar una lista
# no es posible hacer lista2 = lista1, puesto que lista2
# será solo una referencia de lista1 y los cambios hechos en
# lista 1 se verán reflejados en lista2
copiaLista = miListaNumeros

miListaNumeros.append(666)
print(miListaNumeros)
print(copiaLista)

# Para hacer una copia completamente separada de la lista original
# se debe usar el método copy()
copiaLista = miListaNumeros.copy()

miListaNumeros.append(999)
print(miListaNumeros)
print(copiaLista)

# Revertir el orden de la lista
copiaLista.reverse()

# Añadir toda una lista al final de otra
miListaNumeros.extend(copiaLista)
print(miListaNumeros)