'''
	Cadenas de caracteres
'''

# Las cadenas de texto en Python pueden definirse mediante
# comillas simples o dobles
unaCadena = 'Esta es una cadena de texto'
otraCadena = "Esta es otra cadena de texto"

# Lineas múltiples
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Se trata de un arreglo las cadenas de texto
a = "Cadena de texto"
print(a[1])

# Tomar del caracter 2 a 5 (no incluído)
print(a[2:5])

# Indexación negativa de -5 a -2 (no incluído)
print(a[-5:-2])

# Longitud de una cadena
len(a)

# Eliminar espacios al inicio o al final del texto
a = " Cadena de texto "
print(a)
print(a.strip())

# volver todo minúsculas
print(a.lower())

# volver todo mayúsculas
print(a.upper())

# Reemplazar una subcadena dentro de otra cadena
print(a.replace("a","x"))

# Dividir una cadena en subcadenas si encuentra una instancia del separador
print(a.split(","))

# Hallar la ocurrencia de una subcadena dentro de otra
x = "tex" in a
# x = "tex" not in a para decir si no se encuentra
print(x)	# Regresa un booleano si es que aparece 

# Concatenación de cadenas de texto
# en la siguiente se concatena un espacio entre ambas cadenas
cadenaLarga = unaCadena + " " + otraCadena
print(cadenaLarga)

# Como se sabe, no se pueden combinar cadenas de texto y números, sin embargo
# se puede hacer uso del método format()
edad = 36
namen = "Slim Shady"
txt = "Mi nombre es {} y tengo {} años"
print(txt.format(namen, edad))
# Pueden usarse varios y cada uno se colocará en su lugar

# O también formatear la base numérica con la que se muestran los valores
elDiez = 10
print("Decimal {:}".format(elDiez))
print("Binario {:b}".format(elDiez))
print("Octal {:o}".format(elDiez))
print("Hexadecimal {:x}".format(elDiez))

# Caracteres de escape (muy similares a C-ANSI)
'''
\'		comilla simple
\\		diagonal inversa
\n		salto de línea
\r		caracter de retorno
\t		tabulador
\b		backspace
\ooo	valor en base octal
\xhh	valor en base hexadecimal
'''
# Estos caracteres de escape se pueden ignorar con el uso de cadenas raw
print(r"Esta es una cadena cruda \n")

# Métodos adicionales de cadena de caracteres
estaCadena = "esta es una cadena de caracteres adicional"

# Coloca una mayúscula a la primera letra de la cadena
estCadena.capitalize()

# Contabilizar el número de ocurrencias de una subcadena
estCadena.count("esta")

# Buscar la primera ocurrencia de una subcadena
estaCadena.find("cadena")
estaCadena.index("cadena")

# Hacer una partición de la cadena, tomando en cuenta una subcadena
# Este método devuelve una tupla seccionando la cadena de caracteres en 3:
# antes de la subcadena, la subcadenda y posterior a la subcadena
x = estaCadena.partition("cadena")
print(x)

'''
	Métodos para verificar si todos los elementos de una cadena son:
	Alfanuméricos		.isalnum()
	Alfabéticos			.isalpha()
	Números				.isdigit()
	Letras minúsculas	.islower()
	Letras mayúsculas	.isupper()
	Espacios			.isspace()
	Numéricos			.isnumeric()	Se consideran también como ² y ¾ por ejemplo
'''
