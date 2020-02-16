'''
    HERENCIA
    La herencia permite definir una clase que hereda todos los métodos y propieades
    de otra clase
    
    Clase Padre, es la clase de que se heredará, también llamada clase base
    Clase Hija, es la clase que hereda, también llamada clase derivada
'''

# Crear una clase llamada Persona
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        
    def imprimirNombre(self):
        print(self.nombre, self.apellido)
        
# Utilzar la clase persona para crear un objeto y asignar valores
x = Persona("Juan", "Nepomuceno")
# Usar el método de la clase
x.imprimirNombre()

# Crear una clase hija
class Estudiante(Persona):
    # Se crea la función __init__()
    def __init__(self, nombre, apellido, anno):
        # Llamando a la función __init__() de la clase Persona
        Persona.__init__(self, nombre, apellido)
        # Puede usarse la función super() en lugar de Persona
        # esta permite obtener los métodos y atributos de la clase padre
        # Luego puede agregarse propiedades exclusivas de la clase hija
        self.graduacion = anno
        
    def bienvenida(self):
        print("Bienvenido ", end = "")
        super().imprimirNombre()
        print("Clase ", self.graduacion)
        

x2 = Estudiante("Maximiliano", "de Habsurgo", 1860)
x2.bienvenida()