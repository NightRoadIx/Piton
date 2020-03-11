# Programa para revisar si una cadena es un palindroma
import re

# Cadena a verificar
cad = 'Satan oscillate my metallic sonatas'
cad = cad.casefold()

# Utilizando la librería re eliminar todos los espacios
cad = re.sub(r"\s+", "", cad)

# Convertir la cadena en una lista
lista01 = list(cad)
# Copiar en otra lista
lista02 = lista01.copy()
# Revertir la segunda lista
lista02.reverse()

# Verificar si ambas listas son iguales
if lista01 == lista02:
    print("Palindromo")
else:
    print("No palindromo")