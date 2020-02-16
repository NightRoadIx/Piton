'''
    FUNCIONES LAMBDA
    La función lambda es una pequeña función anónima
    que puede tomar cualquier número de argumentos
    pero solo tiene una expresión.
    Se declara:
        
        lambda argumentos : expresión
    
'''

# Se declara una función que suma 10 al argumento que se pasa
x = lambda a : a + 10
# Mandar a llamar a la función e imprimirla
print( x(5) )

# Ahora declarar una función con dos argumentos
x2 = lambda a, b : a * b
print( x2(5, 6) )

# La utilidad de la funciones lambda, radica en que se pueden usar como funciones
# anónimas dentro de otra función
# Se tiene una función que toma un argumento y que ese argumento será multiplicado
# por un número desconocido
def miFuncion(n):
    return lambda a : a * n

# Ahora entonces, se usa esta definición de función para hacer una función que
# siempre duplique todo lo que se envía
duplicador = miFuncion(2)
print(duplicador(11))
# Por tanto:
# 1.- Se genera una variable que asigna el(los) valor(es) a la función lambda dentro de la función
# 2.- Esa variable ahora funciona como el nombre d ela función, la cual recibe el(los) valor(es) a operar

# Por tanto, se pueden tener a partir de la definición de una sola función, una colección
# de funciones que hacen operaciones diferentes

# Ahora uno que triplica el valor de lo que se envía
triplicador = miFuncion(3)
print(triplicador(11))
