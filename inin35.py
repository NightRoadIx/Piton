'''
    PROGRAMACIÓN ORIENTADA A OBJETOS
    Programa que incluye vvarios concepotos de POO
    en el que se muestra la clasificación taxonómica de un animal (gato).
    La taxonomía se encarga de clasificar a todos los organismos vivos,
    en general se consideran los siguientes grupos principales para
    realizar la clasificiación:
        Dominio
        Reino
        Clase
        Orden
        Familia
        Género
        Especie
    (En algunas de ellas se presnetan subclasificiones, pero estos son los
    grupos generales)
'''

class Reino:
    # ATRIBUTOS
    # Los atributos son variables que definen a una clase, en Python se les
    # conoce como Variables de Clase
    # Pueden ser de tipo ocultas o privadas, esto es que no pueden ser manejadas
    # fuera de la misma clase
    __Dominios = ["Archae", "Bacteria", "Eukarya"]
    __Reinos = ["Protista","Fungi","Plantae","Animalia"]
    # Los siguientes atributos pueden ser modificados fuera de la clase
    dominio = ""
    reino = ""
    
    # MÉTODOS
    # Los métodos son todas aquellas funciones que realizan alguna acción
    # dentro de la clase, y pueden modificar o ingresar a sus atributos
    # Uno de los métodos más representativos en las clases se trata del
    # constructor
    def __init__(self):
        # El constructor en este caso inicia los atributos a cadena vacía
        # OJO: En este caso, se iniciaron los atributos tanto en la clase
        # como en el constructor, solo para ejemplificar
        self.dominio = ""
        self.reino = ""
    # Otro método representativo de la POO es el Destructor, el cual se 
    # encarga de limpiar la memoria al eliminar el objeto 
    # OJO: En Python (al igual que muchos otros lenguajes que soportan la 
    # POO como C# o Java) los destructores no son tan importantes, ya que existe
    # algo conocido como "recolector de basura" que se encarga de eliminar 
    # los objetos y limpiar la memoria cuando sea necesario
    # El destructor por lo general se manda a llamar cuando se termina el programa
    # o mediante la instrucción:
    # del objeto
    def __del__(self):
        print("Se ha llamado al destructor de reinos")
    # Otro método importante es el de impresion __str__, el cual se manda a
    # llamar cuando se imprime el objeto creado a partir de la clase
    # Debe regresar una cadena de texto
    def __str__(self):
        return "Dominios: {} \nReinos  : {}".format(self.__Dominios, self.__Reinos)
    # Método para verificar que exista el Dominio ingresado por el usuario
    def verificarDominio(self, dom):
        for domine in self.__Dominios:
            if domine.lower() == dom:
                return False
        return True
    # Método para verificar que exista el Reino ingresado por el usuario
    def verificarReino(self, rey):
        for rein in self.__Reinos:
            if rein.lower() == rey:
                return False
        return True
    # Método para asignar valores a Dominio
    def setDominio(self, dom):
        self.dominio = dom
    # Método para asignar valores a Reino
    def setReino(self, rey):
        self.reino =rey

# Se generará ahora la clase Animalia, la cual será clase hija de Reino
# Esto es que heredará todos los atributos y métodos
# de la clase padre
class Animalia(Reino):
    # Atributos
    __Clases = ["Aneelida", "Arthropoda", "Brachiopoda", "Bryozoa", "Chordata", "Echinodermata", "Hemicohordata", "Loricefera", "Mammalia", "Mollusca", "Nematoda", "Phoronida", "Rhombozoa", "Tardigrada"]
    clase = ""
    
    # Métodos
    def __init__(self):
        self.clase = ""
    def __str__(self):
        return "Clases: {}".format(self.__Clases)
    # Método para verificar que exista la Clase ingresado por el usuario
    def verificarClase(self, claseAnimal):
        for clas in self.__Clases:
            if clas.lower() == claseAnimal:
                return False
        return True
     # Método para asignar valores a Clase
    def setClase(self, claseAnimal):
        self.clase = claseAnimal

class Mammalia(Animalia):
    # Atributos
    __Ordenes = ["Artilodacta","Carnivora","Chiroptera","Dinocerata","Litopterna","Mulituberculata","Primates","Rodentia","Scadentia"]
    orden = ""
    
    # Métodos
    def __init__(self):
        self.orden = ""
    def __str__(self):
        return "Ordenes: {}".format(self.__Ordenes)
    # Método para verificar que exista el Orden ingresado por el usuario
    def verificarOrden(self, ordenAnimal):
        for ord in self.__Ordenes:
            if ord.lower() == ordenAnimal:
                return False
        return True
     # Método para asignar valores a Orden
    def setOrden(self, ord):
        self.orden = ord

class Carnivora(Mammalia):
    # Atributos
    __Familias = ["Canidae", "Felidae", "Herpestidae","Hyanidae","Mustelidae","Ursidae"]
    familia = ""
    
    # Métodos
    def __init__(self):
        self.familia = ""
    def __str__(self):
        return "Familias: {}".format(self.__Familias)
    # Método para verificar que exista la Familia ingresado por el usuario
    def verificarFamilia(self, familiaCarn):
        for fam in self.__Familias:
            if fam.lower() == familiaCarn:
                return False
        return True
     # Método para asignar valores a Familia
    def setFamilia(self, fam):
        self.familia = fam

class Felidae(Carnivora):
    # Atributos
    __Generos = ["Acinonyx", "Caracal", "Felis", "Leopardus", "Lynx", "Puma", "Panthera"]
    genero = ""
    
    # Métodos
    def __init__(self):
        self.genero = ""
    def __str__(self):
        return "Generos: {}".format(self.__Generos)
    # Método para verificar que exista el Genero ingresado por el usuario
    def verificarGenero(self, generofelid):
        for gen in self.__Generos:
            if gen.lower() == generofelid:
                return False
        return True
     # Método para asignar valores a Genero
    def setGenero(self, gen):
        self.genero = gen

# La clase final Gato que es hija de Felidae, hija de Carnivora, hija de Animalia, hija de Reino
class Gato(Felidae):
    # Atributos
    especie = ""
    raza = ""
    
    # Métodos
    def __init__(self):
        self.especie = ""
        self.raza = ""
    def setEspecie(self, espec):
        self.especie = espec
    def setRaza(self, raz):
        self.raza = raz
    # Método parta imprimir todo
    def imprimirArbol(self):
        print("Dominio : " + self.dominio)
        print("Reino   : " + self.reino)
        print("Clase   : " + self.clase )
        print("Orden   : " + self.orden)
        print("Familia : " + self.familia)
        print("Genero  : " + self.genero)
        print("Especie : " + self.especie)
        print("Raza    : " + self.raza)
    

# PROGRAMA PRINCIPAL
# Para probar, se crea un objeto de la clase Reino
t = Reino()
# Se muestra el método __str__
print(t)
# El destructor
del t

# Una vez probado esto, se genera la clase inicial
nuevoGato = Gato()
'''
Probar con 
			 * Dominio: Eurkarya
			 * Reino  : Animalia
			 * Clase  : Mammalia
			 * Orden  : Carnivora
			 * Familia: Felidae
			 * Genero : Felis
			 * Especie: Catus
			 * Raza   : Hay varias... Angora, Abisinio, Burmés, Bengala, Mnax, Himalayo, Pixie, Ocicat, Oriental, Siamés, Siberiano, etc...
'''
# Ingresar Dominio (ver la forma en que se utiliza el método de verificiación)
tmp = ""
while nuevoGato.verificarDominio(tmp):
    tmp = input("Ingresar dominio: ");
# Una vez que ya se haya salido del ciclo, se asigna
nuevoGato.setDominio(tmp)

# Ingresar Reino
tmp = ""
while nuevoGato.verificarReino(tmp):
    tmp = input("Ingresar reino: ");
# Una vez que ya se haya salido del ciclo, se asigna
nuevoGato.setReino(tmp)

# Ingresar Clase
tmp = ""
while nuevoGato.verificarClase(tmp):
    tmp = input("Ingresar clase: ");
# Una vez que ya se haya salido del ciclo, se asigna
nuevoGato.setClase(tmp)

# Ingresar Orden
tmp = ""
while nuevoGato.verificarOrden(tmp):
    tmp = input("Ingresar orden: ");
# Una vez que ya se haya salido del ciclo, se asigna
nuevoGato.setOrden(tmp)

# Ingresar Familia
tmp = ""
while nuevoGato.verificarFamilia(tmp):
    tmp = input("Ingresar familia: ");
# Una vez que ya se haya salido del ciclo, se asigna
nuevoGato.setFamilia(tmp)

# Ingresar Genero
tmp = ""
while nuevoGato.verificarGenero(tmp):
    tmp = input("Ingresar genero: ");
# Una vez que ya se haya salido del ciclo, se asigna
nuevoGato.setGenero(tmp)

# Ingresar Especie y Raza
tmp = input("Ingresar especie: ")
nuevoGato.setEspecie(tmp)
tmp = input("Ingresar raza   : ")
nuevoGato.setRaza(tmp)

# Una vez ingresado todo, se imprime
nuevoGato.imprimirArbol()

# DE ESTA FORMA EL PROGRAMA PODRÍA SER AMPLIADO PARA INCLUIR TODAS LAS POSIBLES
# ESPECIES QUE HAN DISO REGISTRADAS, A PARTIR DE UNAS CUANTAS CLASES