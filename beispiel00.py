# python --version
# conda -V

# Imprimir en Python 3
print("Impresión")

# Indentación
if 5 > 2:
 print("Cinco es más grande que dos")

# Variables en Python
x = 5
y = "Esta es una cadena"

# Asignación de variables múltiples
a, b, c = "Naranja", "Banana", "Cereza"

# Concatenación de variables cadena de caracteres
print("Las cadenas son: " + a + ", " + b + ", " + c)
# No es posible combinar cadenas de caracteres con números

# Comentario de una línea
'''
Comentarios de varias líneas
'''

# Funciones y variables globales
r = "fantástico"

# Definición de una función
def miFun():
 # puede re-definirse una variable dentro de una función
 # r = "peligroso"
 # o usar la palabra clave 'global' para transformar la variable a global
 print("Python es " + r)

# Llamado a la función
miFun()

'''
Tipos de Datos:
Texto			str
Numérica		int, float, complex
Secuencial		list, tuple, range
Mapeo			dict
Set				set, frozenset
Booleana		bool
Binaria			bytes, bytearray, memoryview
'''
# Utilizar type() para conocer el tipo de variable

'''
x = "Hello World"
x = 20
x = 20.5
x = 1j
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
x = {"name" : "John", "age" : 36}
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
x = True
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))
'''

# Se puede usar una especie de "cast"

# Tipos numéricos
# int, enteros
# float, flotantes (puede usarse XeY para mostrar una notación científica
# complex, complejos, se usa j para indicar la parte imaginaria

# Números aleatorios
import random

print(random.randrange(1,10))

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
# x = "tex" not in a
print(x)	# Regresa un booleano si es que aparece 

# Como se sabe, no se puedne combinar cadenas de texto y números, sin embargo
# se puede hacer uso del método format()
edad = 36
namen = "Slim Shady"
txt = "Mi nombre es {} y tengo {} años"
print(txt.format(namen, edad))
# Pueden usarse varios y cada uno se colocará en su lugar

# Caracteres de escape
'''
\'		comilla simple
\\		diagonal inversa
\n		salto de línea
\r		caracter de retorno
\t		tabulador
\b		backspace
'''
# Métodos de cadena
# https://www.w3schools.com/python/python_strings.asp

# Valores booleanos
# La mayoría de los valores son verdaderos
# bool(5)
# excepto algunos no lo son:
# False, None, 0, "", (), [], {}


# Operaciones
'''
 +		suma
 -		resta
 *		multiplicación
 /		división
 %		módulo
 **		exponente
 //		división floor
 
 &		AND
 |		OR
 ~		NOT
 ^		XOR
 >>		Desplazamiento bits a la derecha
 <<		Desplazamiento bits a la izquierda
 
 and	y
 or		o
 not	no 
 
'''

# List:			es una colección que está ordenada y es cambiable. Permite miembros duplicados
# Tuple:		es una colección que está ordenada y no es cambiable. Permite miembros duplicados
# Set:			es una colección que no está ordenada ni tampoco indexada. No permite miembros duplicados
# Dictionary:	es una colección la cual está ordenada, es cambiable y esta indexada. No permite miembros duplicados

estaLista = ["manzana", "banana", "cereza"]
# Ingresar a la lista
print(estaLista[1])
# con indices negativos
print(estaLista[-1])
# De la misma forma, se puede usar un intervalo (sin incluir el valor final)
# y usar :X para iniciar desde el elemento 0 hasta el X-1

# puede reemplazarse el elemento al especificar
estaLista[1] = "plátano"

# Recorrer la lista
for x in estaLista:
 print(x)

# Verificar si un elemento existe en la lista
if "manzana" in estaLista:
 print("Si, 'manzana' existe en esta lista")

# Tamaño de la lista
print(len(estaLista))

# Añadir elementos
estaLista.append("naranja")

# Insertar elementos 
estaLista.insert(1, "kiwi")

# Eliminar elementos
# estaLista.remove("banana")
# estaLista.pop()
# del estaLista[n] ó del estaLista
# estaLista

# Copia listas
miLista= estaLista.copy()

# Concatenar o unir listas
# Usar el operador '+'

# Las matrices pueden ser representadas como listas anidadas
a = [[1, 2, 3],
     [4, 5, 6],
	 [7, 8, 9]
    ]
print(a[1])

# Tuplas
estaTupla = ("manzana", "banana", "cereza")
print(estaTupla)

# Acceder a los elementos de la tupla
# estaTupla[1]
# de la misma forma se puede usar indexación negativa

# Las tuplas no pueden ser modificadas
# sin embargo es posible cambiar una tupla a una lista, modificar la lista y luego cambiarla a tupla
x = ("manzana", "banana", "cereza")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

# Mismo comportamiento en métodos for
# e if

# Las tuplas pueden dividirse
rec = ("Nepomuceno", "Juan", (5, 15, 1803))
apellido, nombre, ecNac = rec


# Sets
esteSet = {"manzana", "banana", "cereza"}

# Los elementos en los Sets no tienen un índice, por lo que no se puede acceder con un números
# por lo que se tiene que usar for o if para saber si hay un elemento en el Set

# Se puede usar el método add para añadir elementos
esteSet.add("naranaja")

# o el método update
esteSet.update(["naranja", "mango", "uvas"])



# sentencia if
a = 33
b = 33
if b > a:
 print("b es mayor que a")
elif a == b:
 print("a y b son iguales")
else
 print("a es mayor que b")

# aquí se usan las palabras 'and' 'or' 'not'


# sentencia while
i = 1
while i < 6:
 print(i)
 i += 1
# Se puede usar la sentencia break para terminar el ciclo
# if i == 3: break

# sentencia continue
i = 0
while i < 6:
 i += 1
 if i == 3:
  continue
 print(i)

# sentencia for
for x in "banana":
 print(x)

# sentencia range()
for x in range(6):
 print(x)

for x in range(2,6):
 print(x)

for x in range(2, 30, 3):
 print(x)

adjetivos = ["rojo", "grande", "frio"]
frutas = ["manzana", "banana", "cereza"]

for x in adjetivos:
 for y in frutas:
  print(x, y)

# FUNCIONES
def miFuncion(fname):
 print(fname)

miFuncion("Parametro")

def miFuncion2(pais = "Suecia"):
 print("To soy de " + pais)

miFuncion2()
miFuncion2("Brasil")

# Valores de retorno
def miNuevaFun(x):
 return 5 * x

print(miNuevaFun(4))

# Enviar valoes con la palabra clave
def miFun3(nino3, nino2, nino1):
 print("El niño más pequeño es " + nino3)

miFun3(nino1 = "Emil", nino2 = "Tobias", nino3 = "Linus")

def miFun4(*ninos):
 print("El niño más pequeño es: " + ninos[2])

miFun4("Emil", "Tobias", "Linus")

# Recursividad
def recurse(k):
 if(k > 0):
  resultado = k + recurse(k-1)
  print(resultado)
 else:
  resultado = 0
 return resultado

print("Recursivida\'")
recurse(6)

# Funciones lambda
# Define funciones de 1 sola línea
x = lambda a : a + 10
print(x(5))

def miFun5(n):
 return lambda a : a * n

result1 = miFun5(2)
print(result1(11))

result2 = miFun5(3)
print(result2(11))


# Arreglos en el Python
# muy similar a listas
# arreglo = ["eleme1", "elem2", "elem3"]
# .append("ElementoNuevo") METODO PARA AÑADIR
# .pop(n) ELIMINAR ELEMENTOS DEL ARREGLO
# .remove("Elemento") REMOVER ELEMENTOS



# POO EN PYTHON
# Definir una clase
class miClase:
 x = 5		# Definir un atributo

# Crear un objeto
p1 = miClase()
# Mostrar el atributo
print(p1.x)

# La función __init__() {constructor}
# Esta función es llamada de manera automática cada que se usa una clase
# para crear un objeto
class Persona:
 def __init__(self, nombre, edad):
  self.nombre = nombre
  self.edad = edad
 
 def miFuncionClase(self):
  print("Hola mi nombre es " + self.nombre)
# El parametro self es una referencia a la instancia de clase actual, y es utilizada
# para acceder a variables que pertenecen a la clase
# No es necesario que se llame self, pero siempre debe ser el primer argumento de la función

p1 = Persona("Juan Nepomuceno", 36)

print(p1.nombre)
print(p1.edad)
p1.miFuncionClase()

# Se puede cambiar los elementos de forma así salvaje
p1.edad = 40
print(p1.edad)

# Se puede eliminar atributos de los objetos usando la palabra 'del'
# del p1.edad
# incluso borrar los objetos
# del p1

# Herencia
class Persona:
 def __init__(self, nom1, nom2):
  self.nombre = nom1
  self.apellido = nom2
 
 def imprimeNombre(self):
  print(self.nombre, self.apellido)

x = Persona("Juan", "Nepomuceno")
x.imprimeNombre()

# Crear una clase hija
class Estudiante(Persona):
 pass # Se usa si no se desea agregar ni un método o atributo adicional

x = Estudiante("Mike", "Olsen")
x.imprimeNombre()


# EXCEPCIONES
try:
 print(f)
except NameError:
 print("La variable f no está definida")
except:
 print("Algo más malio sal")

try:
 f = open("demofile.txt")
 f.write("Lorem Ipsum")
except:
 print("Algo salió mal al intentar esceribir el archivo")
finally:
 print("Cerrando archivo")
 f.close()

# Entrada de datos
nombreUsuario = input("Ingrese nombre de usuario: ")
print("El nombre es: " + nombreUsuario)



# FECHAS
import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
# Ver los formatos del método strftime()



# Manejo de JSON Data
# Java Script Object Notation
import json

# Crear un JSON
x = '{"nombre" : "Juan Nepomuceno", "edad" : 30, "ciudad" : "Nocupétaro"}'

# Obtener el JSON
y = json.loads(x)

# El resultado es una variable tipo diccionario
print(y["edad"])


# Ahora crear un diccionario (o list, tuple, string, int, float) para pasar a JSON
x = {"nombre" : "Juan Nepomuceno", "edad" : 30, "ciudad" : "Nocupétaro"}

# convertir a JSON
y = json.dumps(x)

# El resultado es una cadena JSON
print(y)

# Convertir un objeto Python que contenga todos los tipos válidos de Python
x = {
"nombre": "Juan Nepomuceno", 
"edad" : 30,
"casado" : True,
"divorciado" : False,
"hijos" : ("Guadalupe Almonte", "Morelitos"),
"mascotas" : None,
"autos" : [
 {"modelo" : "BMW 230", "mpg" : 27.5},
 {"modelo" : "Ford Edge", "mpg" : 24.1}
]
}

print(json.dumps(x))

# Dar formato al JSON
print(json.dumps(x, indent=4))



# MANEJO DE ARCHIVOS
f = open("miArchivo.txt", "w")
'''
 Opciones:
 w		Escribir
 r		Leer
 x		Crear
 a		Añadir
'''
f.write("Este es un nuevo archivo")
'''
for i in range(10):
 f.write("Esta es la línea %d\r\n" %(i+1))
'''


'''
for k in range(101, 111):
 f.write("{:4d} {:6d}".format(k, k**2))
 f.write('\n')
f.close()
'''
# Muy importante, cerrar el archivo
f.close()

