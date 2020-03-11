# Función para definir si es o no un año bisiesto, la función regresa un booleano
def bisiesto(anno):
    return ( (anno % 4 == 0) and (anno % 100 != 0) or (anno % 400 == 0) )

# Recibir un entero que representa un año
anno = int(input("Ingrese un año: "))
# Verificar si es un año bisiesto
resp = " es bisiesto" if bisiesto(anno) else " no es bisiesto"
# Escribir si es bisiesto o no
print("El año " + str(anno) + resp)
