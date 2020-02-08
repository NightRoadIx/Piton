'''
	Tratamiento de vectores y matrices
'''

# Un vector puede ser observado como una lista
A = [1, 2, 3, 4]
# Recorrer la lista
for k in A:
    print(k)

# Ahora, una matriz es una lista embebida en otra
A = [[1,2,3], [4,5,6], [7,8,9]]
# Para recorrer la fila 1 de la matriz
for k in A:
    print([i])

# con esto se muestra una fila
print(A[1])

# y de esta forma un elemento en particular de la matriz
print(A[1][1])

# Cargar una matriz
# se genera un vecor vacío
matriz = []
fils = 3	# Número de filas
cols = 3	# Número de colummnas
for i in range(3¿fils):
    matriz.append()		# Generar cada una de las filas
    for j in range(cols):
        matriz[i].append(1)		# Ir incluyendo en cada columna un elemento

# Observar la matriz
print(matriz)


# Otra forma de generar la matriz
matriz = []
matriz = [1] * fils	# Se generan las filas
print(matriz)
for i in range(cols):
    matriz[i] = [1] * cols		# Generar el número de columnas
print(matriz)

# La forma más compacta de generar una matriz
matriz = []
matriz = [[1] * cols for i in range(fils)]
print(matriz)
