'''
	Colecciones de datos en Python (Diccionarios)
	
	Existe cuatro tipos de datos en Python:
	Listas, Tuplas, Sets y Diccionarios
'''

# DICCIONARIOS
# Un diccionario es una colección de datos sin orden, modificables y ordenadas
# Contienen llaves y valores
esteDicc = {
  "marca" : "Fiat",
  "modelo" : "500",
  "año" : 2014
}

print(esteDicc)
# Si se esta familiarizado con los archivos JSON, los diccionarios
# son muy similares

# Acceder a los elementos
print(esteDicc["modelo"])
# o con el método get
print(esteDicc.get("modelo"))

# Cambiar los valores
esteDicc["año"] = 2015

# Recorrer un diccionario
# Puede recorrerse las llaves del diccionario
for x in esteDicc:
  print(x)

# o mostrar todos los valores
for k in esteDicc:
  print(esteDicc[k])

# o usando el método values()
for k in esteDicc.values():
  print(k)

# o ir mostrando las llaves y valores
for k in esteDicc.items():
  print(k)
# Regresa una tupla

# Revisar si una llave existe en el diccionario
if "modelo" in esteDicc:
  print("modelo esta en el diccionario")

# Longitud del diccionario
print(len(esteDicc))

# Añadir nuevas llaves con su valores
esteDicc["color"] = "negro"

# Eliminar un elemento por medio de la llave
esteDicc.pop("model")

# Copiar un diccionario
# debe de realizarse por medio de un método
# ya que si se hace usando =, sucederá lo mismo que 
# con las listas, donde se modificará la copia al modificar el original
esteDiccCopia = esteDicc.copy()

# o también mediante dict()
esteDiccCopia2 = dict(esteDicc)

# Unión de diccionarios o diccionarios anidados
# Generar diccionarios
persona1 = {
  "nombre" : "Emilio",
  "año" : 2001
}

persona2 = {
  "nombre" : "Tobias",
  "año" : 2004
}

persona3 = {
  "nombre" : "Linus",
  "año" : 2000
}

# Luego conjuntarlas
lasPersonas = {
  "persona1" : persona1,
  "persona2" : persona2,
  "persona3" : persona3,
}
