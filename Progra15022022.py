
# Se crea una lista vacía
B = []
for i in range(0, 100+1, 3):
  # B[j] = i; como en C, C++, C#
  # Agregar elementos a la lista
  B.append(i)

# Imprimimos la lista generada
print(B)

# Esto se puede realizar con list comprehension:
B = [i for i in range(0, 100+1, 3)]
print(B)

# En su forma máxima
# [elemento ciclo_generador condición]
B = [i for i in range(101) if i % 3 == 0]
print(B)