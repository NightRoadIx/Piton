'''
	Manejo de estructuras de control
'''

# ESTRUCTURA DE DECISIÓN
a = 23
b = 43

if a > b:
  print("{:d} es mayor que {:d}".format(a, b))
elif a < b:
  print("{:d} es mayor que {:d}".format(b, a))
else:
  print("Ambos números son iguales")
# Se debe considerar la "indentación"
# esto es colocar espacio o espacios 
# para sustituir a las llaves del lenguaje C

# ESTRUCTURAS DE CICLOS
# Ciclo while
i = 1
while i < 6:
  print(i)
  i += 1

# Utilizando la instrucción break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Utilizando la instrucción continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)


# Ciclo for
# Puede usarse la instrucción range()
# para indicar inicio, fin y pasos que dará el for
for k in range(0, 10, 1):
  # en lenguaje c sería algo como for(k = 0; k < 10; k++)
  print(k)

# Puede usarse para recorrer letra a letra una cadena de texto
for k in "anaconda":
  print(k)
