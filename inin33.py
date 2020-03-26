'''
    LIST COMPREHENSION
    y entrada múltiple de datos
'''

# La list comprehension es una manera elegante de generar listas en Python
# Además funcionan para ingresar datos de manera múltiple

# Supongamos que se dese acrear una lista con los múltiplos de 5 del 1 al 14
multipl = [n*5 for n in range(1,15)]
# Para desmenuzar esta instrucción:
# Todo está dentro de [], entonces el producto es una lista
# Luego se multiplizará n*5, lo cual inidica que el resultado será un número de este tipo
# psoteriormente se coloca una instrucción for que itera en n, desde 1 hasta 14
# Lo cual genera la lista de datos buscada

# Incluso se pueden utilizar condicionales en la generación de listas
# lo siguiente genera una lista con los múltiplos de 3 de los números pares
multipl2 = [n*3 for n in range(1,21) if n%2 == 0]

# Lo siguiente es un poco más complejo, pero genera los cubos de los números
# impares y los cuadrados de los números pares
multipl3 = [n**2 if n%2 == 0 else n**3 for n in range(1,16)]

# Ingresar valores varios, separados por un espacio y se termina con Enter
lista = [int(x) for x in input("Ingresar valores separados por un espacio: ").split()]
# La instrucción anterior se puede desmenuzar de la siguiente forma:
# Todo se encuentra dentro de [] lo cual indica que se genera una lista
# después se indica que el valor de la lista x será un int, creado a partir del constructor int()
# posteriormente se indica con un for que se recorrera la variable x en un input el cual se separará por medio de la función split() que separa los valores de una cadena de texto, usando como separadaor el espacio 

