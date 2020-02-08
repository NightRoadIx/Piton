'''
	Programación orientada a objetos en Python
'''
# Creación de una clase
class MyClass:
    x = 5

# Crear un objeto (instanciar)
p1 = MyClass()
# Imprimir el valor del argumento
print(p1.x)


'''
Sin embargo este uso simple de objetos no tienes validez en la vida real
por lo que se introduce un nuevo tipo de método, __init__()
el cual es siempre ejecutado cuando la clase se instancia

El método __init__() se utiliza para asignar valores a las propiedades del objeto
|u otras operaciones que son necesarias cuando el objeto es creado
'''

class Persona:
    def __init__(self, nombre, edad):
        # self indica que es el propio objeto
        # cuyos atributos de nombre y edad se asignan a lo que se envía como parámetros
        self.nombre = nombre
        self.edad = edad
        
        # Se incluye un método
    def miFuncion(self):
        # Se recibe "self" el cual indica al mismo objeto
        # y es utilizado para ingresar a las variables que pertenecen a la clase
        print("Hola mi nombre es " + self.nombre + " y tengo " + str(self.edad) + " años")

# Se instancia el objeto con valores iniciales
p1 = Persona("Juan Nepomuceno", 36)

print(p1.nombre)
print(p1.edad)

p1.miFuncion()


# Se pueden hacer modificaciones en las propiedades/atributos del objeto
p1.edad = 40
p1.miFuncion()