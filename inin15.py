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



# HERENCIA MÚLTIPLE
# A diferencia de C# y Java, Python permite la herencia múltiple (como C++)
# esto es, que una clase puede heredar atributos de múltiples clases
class MiSuperClase1():
    def metodo_1(self):
        print("metodo_1 metodo llamado")
  
class MiSuperClase2():
    def metodo_2(self):
        print("metodo_2 metodo llamado")
 
# Clase que hereda las 2 clases anteriormente definidas
class MiClase(MiSuperClase1, MiSuperClase2):
    def metodo_3(self):
        print("metodo_3 metodo llamado")
 
# Se crea el objeto "c" y luego se llama al metodo_1 y metodo_2 heredados de las 2 primeras clases
c = MiClase()
c.metodo_1()
c.metodo_2()


# Otro ejemplo de herencia múltiple
class Telefono:
    "Clase teléfono"
    def __init__(self,numero):
        self.numero=numero
    def telefonear(self):
        print('llamando')
    def colgar(self):
        print('colgando') 
    def __str__(self):
        return self.numero	

class Camara:
    "Clase camara fotográfica"
    def __init__(self,mpx):
        self.mpx=mpx
    def fotografiar(self):
        print('fotografiando')        
    def __str__(self):
        return self.mpx
class Reproductor:
    "Clase Reproductor Mp3"
    def __init__(self,capcidad):
        self.capacidad=capcidad
    def reproducirmp3(self):
        print('reproduciendo mp3')                  
    def reproducirvideo(self):
        print('reproduciendo video')                  
    def __str__(self):
        return self.capacidad	

class Movil(Telefono, Camara, Reproductor):
    def __init__(self,numero,mpx,capacidad):
        Telefono.__init__(self,numero)
        Camara.__init__(self,mpx)
        Reproductor.__init__(self,capacidad)
    def __str__(self):
        return "Número: {0}, Cámara: {1},Capacidad: {2}".format(Telefono.__str__(self),Camara.__str__(self),Reproductor.__str__(self))