'''
    Expresiones regulares (RegEx)
    Se trata d euna sencuencia de caracteres que forman un patrón de búsqueda
    RegEx puede ser utilizado para revisar si una cadena de texto contiene un patrón específico
'''
# En primer lugar se tiene que importar el módulo "re"
import re

# Generar una cadena de texto
testo = "La lluvia en el País Vasco caia"
# Se utiliza el método search() que busca la cadena que se le proporciona en un texto
# Si hay más de una ocurrencia, solo la primera será almacenada
# Hallar la ocurrencia de espacios en el texto
x = re.search("lluvia", testo)
# Aquí se muestra el objeto
print(x)
# Este objeto contiene propieades y métodos que contienen más información
# Las posiciones en donde se localiza lo que se esta buscando
print(x.span())
# El texto en el que se esta buscando
print(x.string)
# El texto que se localizo
print(x.group())

# Una vez generado el objeto de búsqueda, se pueden usar diferentes métodos
# Para la primera ocurrencia
print("El primer caracter de espacio aparece en la posición ", x.start())

# También puede usarse la función findall() para hallar todas las ocurrencias
x2 = re.findall("ia", testo)
print(x2)
# Si no se encuentran ocurrencias, se retorna una lista vacía

# Si se desea partir la cadena tomando la subcadena como límite y genera una
# lista con las palabras
x3 = re.split("\s", testo)
print(x3)

# La función sub() permite reemplazar las ocurrencias con algún otro texto
# Lo siguiente substituye el espacio por un "9"
x4 = re.sub("\s", "9", testo) 
print(x4)

# se puede especificar cuántos reemplzaos se deben realizar
x4b = re.sub("\s", "9", testo, 2) 
print(x4b)


'''
    METACARACTERES
    Caracteres con significado especial
    []		Set de caracteres
    \		Secuencia especial
	.		Cualquier caracter (excepto el de nueva línea)
	^		Inicia con
	$		Termina con
	*		Cero o más ocurrencias
	+		Una o más ocurrencias
	{}		Exactamente el número específico de caracteres
	|		OR
'''

'''
	SETS DE CARACTERES
	
	[arn]		Este set hace la búsqueda donde uno de los caracteres está presente [a,r,n]
	[a-n]		Este set hace la búsqueda de todas las letras minúsculas entre el intervalo a-n, inclusive
	[^arn]		Este set hace la búsqueda de todas las letras, excepto a,r,n
	[a-zA-Z]	Este set hace la búsqueda de todas las letras minúsculas entre el intervalo a-n, inclusive, minúsculas y mayúsculas
'''

'''
	SECUENCIAS ESPECIALES
	\A		Considera si los caracteres especificados están al inicio de la cadena (\Ael, busca: elefante, el)
	\b		Considera si los caracteres especificados están al inicio o final de la cadena
	\B		Considera si los caracteres especificados NO están al inicio o final de la cadena
	\d		Cualquier digito (0-9)
	\D		Si la cadena NO contiene dígitos
	\s		Espacio
	\S		Si la cadena NO contiene un espacio
	\Z		Considera si los caracteres especificados están al final de la cadena (el\Z, busca: coronel, piel, hotel)
'''






