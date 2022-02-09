# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 09:08:27 2022

@author: s_bio

Introducción al pitooooooooooón!

"""

'''
COMENTARIO LAAAAAAAAAAAAAAAAAAARGO
'''

#%%
y = 5
w = 5.6
pipi = 3.141592653489
cadenas = "Hola todo el mundo"

# ELEMENTOS GRUPEROS
# mutables, ordenados
listass = [3, 4, 4, 5, 6, 7]
otraLista = [y, w, pipi, cadenas, listass]

# inmutables, ordenados
estaTupla = (1, 2, 3, 4, 5)

# inmutables, desordenados
esteSet = {1, 2, 3, 4, 5}

# mutables, ordenados, clave
# como JSON
ditzionario = {'uno' : 'cadenaUno',
               'dos' : 'cadenaDos',
               'tres' : 3,
               'cuatro' : estaTupla}

#%%

# Guardar mi lista original
listaOriginal = tuple(listass)
# Añadir elementos a una lista
listass.append(21)

#%%
# Añadir un elemento al diccionario
ditzionario['cinco'] = 30

#%%

x = y + w

print("Primera celda")

#%%

print("Otra celda")
w = 2

# En las listas SI se pueden cambiar elementos
listass[5] = 14
# En tuplas NO se pueden cambiar
estaTupla[4] = 10

print( type(ditzionario['cuatro']) )

#%%

# + - * / ** //
print(5**2)   # 25

print(3 / 4)  # 0.75
print(3 % 4)  # 3
print(3 // 4) # 0

print(3**6)   # 3 elevado a la 6

#%%
print( 3*("-Hola-\n") )

ws = 3*listass


