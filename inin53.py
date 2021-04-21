# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:09:32 2021

@author: s_bio
"""

#%%
# Recursividad
# La recursividad es cuando una función se llama a si misma. 
# Típicamente, una función recursiva posee una condición de terminación y una
# o varias llamadas recursivas a si misma

# Por ejemplo, para calcular la elevación de un número a un exponente, 
# matemáticamente se puede definir 
def exponente(x, n):
    if n == 0:
        return 1
    else:
        return x * exponente(x, n-1)

#%%
# Esto puede realizarse más rápidamente, si se realizan sucesivamente
# elevar al cuadrado
def exponencialRapida(x, n):
    if  n == 0:
        return 1
    elif n % 2 == 0:
        return exponencialRapida(x*x, n/2)
    else:
        return x * exponencialRapida(x, n-1)


print(exponencialRapida(4, 5))



#%%
# Función recursiva para el cálculo de la serie de Fibonacci
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Muestra el valor de la serie
fib(8)

#%%

# Con la siguiente función se traza todas las llamadas a la función fib
# se escribe una función de orden superior que regresa una nueva función
# la cual imrpime cuando la función fib es llamada
def trazar(f):
    f.indent = 0
    def g(x):
        print('|  ' * f.indent + '|--', f.__name__, x)
        f.indent += 1
        valor = f(x)
        print('|  ' * f.indent + '|--', 'Regresar ', repr(valor))
        f.indent -= 1
        return valor
    return g

fib = trazar(fib)
print(fib(4))