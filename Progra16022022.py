#%%
listaVacia = []
# str()
for i, val in enumerate('Pako Martínez'):
  print(f'{i} -> {val}')
  #listaVacia.append(i)

print(listaVacia)

#%%
# comprensión de listas
listaB = [val for i, val in enumerate('Pako Martinez') if i % 2 == 0]
print(listaB)

#%%
entero = 5
flotante = 3.1416
cadena = 'Pako Martínez'

print(f'Entero: {entero}')
print(f'Flotante: {flotante}')

#%%
matrix = [[1, 2, 3], [4, 5], [7]]

print(len(matrix))
print(range(len(matrix)))

#%%
transposed = []
matrix = [[1, 2, 3, 4], [4, 5, 6, 8]]

print(f'Matriz = {matrix}')
'''
for row in matrix:
  for col in row:
    print(col)
'''
# range(4) = range(0, 4, 1)
for i in range(len(matrix[0])):
    transposed_row = []

    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)

print(f'Transpuesta = {transposed}')

#%%
A = []
for i in range(1,5):
  A.append( list(i*'*') )

print(A)

#%%
'''
[[1],
[1,2],
[1,2,3],
[1,2,3,4]]
'''
A = []
for i in range(1,5):
  fila = []
  for j in range(1, i+1):
    fila.append(j)
    print(j, end = ' ')
  A.append(fila)
  print('')

print(f'Matriz final : {A}')

A[3][2] = 0
print(f'Matriz final : {A}')

#%%
