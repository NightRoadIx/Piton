'''
	Funciones en Python
	Una función es un bloque de código que solo es ejecutada
	cuando es llamada
	Se coloca en un cierto espacio en memoria de código
	Se pueden pasar datos y regresar otros
'''

# Se inicia con la palabra def
def miFuncion():
  print("Esta es la función")

# Una vez definida la función, se puede mandar a llamar
# dentro de la sección "main" del programa
i = 5
## Llamar a la función
miFuncion()

# Incluso se puede ir definiendo en el código cada función
# e irla llamando a partir de ese punto donde fue definida
# en este caso se genera una función que recibe un argumento
# {{SE DEBE RECORDAR QUE SE TIENE QUE ENVIAR EL NÚMERO DE ARGUMENTOS
#   QUE SE ESTÁN SOLICITANDO, DE LO CONTRARIO, MARCARÁ ERROR}}
def laFuncion(nombre):
  print("El nombre es: " + nombre)

laFuncion("Bond, James Bond")

# Valor por defecto de una función
# En el argumento se coloca el valor en caso que no se envie 
# algún valor
def funcionDefault(pais = "Suecia"):
  print("Yo soy de: " + pais)

funcionDefault("Noruega")
funcionDefault("Islandia")
funcionDefault()

# Funciones que regresan valores
# de la misma forma que en otros lenguajes
# se usa la palabra return
def regresaValor(x):
  return 5 * x

# Se manda a llamar
print(regresaValor(3))
print(regresaValor(5))


