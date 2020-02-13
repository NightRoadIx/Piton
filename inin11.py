'''
	Manejo de archivos
	
	Para el manejo de archivos se utiliza  la función
	open() para la apertura del archivo
	dicha función recibe los parámetros:
	
	open("nombreArchivo.ext", "modo")
	
	Donde "nombreArchivo.ext" representa el nombre del archivo a abrir
	se puede incluir la ruta completa del archivo
		modo, representa los diferentes métodos para la apaertura del archivo:
	
	"r"		El archivo abre de solo lectura
	"a"		El archivo abre para agregar datos al final
	"w"		El archivo se abre para escritura, si no existe se crea, si existe se sobreescribe
	"x"		El archivo se abre para su creación, genera un error si el archivo existe
'''

# Abrir el archivo para su escritura
f = open("archivo.txt", "w")

# En caso de que si abra, entonces se procede a escribir
f.write("Ahora el archivo esta bien, pero bien lleno (de basura)")

# Luego se tiene que cerrar por completo
f.close()


# Ahora se abre el archivo para su lectura
g = open("Ahora el archivo esta bien, pero bien lleno (de basura)")

# Leer el archivo e imprimir su contenido
print(g.read())

'''
	En caso de que solo se quiera leer una cierta cantidad de caracteres
	se coloca
	
	g.read(5)		# para la lectura de solo 5 caracteres
	
	En otro caso, si el archivo contiene saltos de línea, esto es 
	diferentes líneas de texto, entonces se puede utilizar la función:
	
	g.readline()
	
	Para la lectura de una sola líneas
	
	ADemás puede usarse:
	
	for x in g:
		print(x)
	
	Para la lectura de todo el archivo, línea por línea

'''

# Cerrar el archivo
g.close()