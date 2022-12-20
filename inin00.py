# Comentario de una sola línea

'''
Comentarios de varias líneas
'''

"""
También se puede hacer esto 
Para comentar varias lineas
"""

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#%% Memoria
# Tipos de variables
# No es necesario colocar que tipo de variable
# Se trata de un lenguaje débilmente tipado
booleana = True
enteros = 5
flotante = 3.1415926539
complejo = 3 + 4j
cadena = "Este es el Pitón!"

# Puede usarse una base diferente
# Decimal
elDiez = 10
elDiezBina = 0b1010
elDiezOcta = 0o12
elDiezHexa = 0xA

# Si uno desea conocer el tipo de dato que se está manejando
type(elDiez)

#%%
# Asignación múltiple de variables
x, y, z = 1, 2, 3
#%%
# Asignación de variables iguales
x = y = z = "Naranja"

#%%
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Entrada de datos
# se utiliza la función input()
variable = input("Aquí va un bonito mensaje: ")
# y el dato se guarda como un string

#%%
# para poder "forzar" a la variable a tomar algún datos
# entonces se usa un especie de "cast"
# (int)variable
variableEntera = int(input("Ingresa un valor entero: "))
variableFlotante = float(input("Ingresa un valor flotante: "))

#%%
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Salida de Datos
# Utilizar la función print()
print("Esta es una salida de datos")

# Para mostrar variables
entero = 5
print(entero)

# Sin embargo si se desea mostrar variables junto con cadenas de texto
# existen varias formas:

# 1. Concatenar cadenas de texto
# Utilizar el "cast" str() para convertir el valor a texto
print("Valor entero: " + str(entero))

# 2. Usar identificadores como en C
print("Un valor flotante %.3f" %flotante)

# 3. Utilizar el método format() para cadenas
# Los números seguidos de :, indican el número de casillas
# que serán asignadas para cada número (esto es muy útil para tablas)
print("Un valor entero {:4}, un valor flotante {:4.3}".format(enteros, flotante))

# 4. Cadenas tipo "f"
print(f"Un valor que no tiene precio: {elDiez}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Operaciones
'''
ARTIMÉTICAS
 +		suma
 -		resta
 *		multiplicación
 /		división flotante
 %		módulo
 **		exponente
 //		división entera
 
 NIVEL DE BITS
 &		AND
 |		OR
 ~		NOT
 ^		XOR
 >>		Desplazamiento bits a la derecha
 <<		Desplazamiento bits a la izquierda
 
 LÓGICAS
 and	y
 or		o
 not	no 
 
'''

# Las divisiones en Python son de dos tipos:
# Divisiones decimales ("normales")}
print(9 / 6)
# O divisiones enteras, en donde solo se obtiene el número entero
# del cociente
print(9 // 6)
# Junto con su módulo o residuo
print(9 % 6)

#%%
# Las operaciones a nivel de bits son las operaciones más rápidas
# que se pueden efectuar en la ALU
# Permiten realizar operaciones lógicas a nivel de bits
# Suponiendo 9 = 1001
# 			12 = 1100
# Operación and
print(9 & 12)	# = 8  = 1000
print(9 | 12)	# = 13 = 1101
print(9 ^ 12)	# = 5  = 0101
print(9 >> 2)	# desplazando 2 bits, queda 00000010 = 2
print(9 << 2)	# desplazando 2 bits, queda 00100100 = 36
