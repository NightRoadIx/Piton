class MiClase:
    # # # # # # # ATRIBUTOS # # # # # # #
    '''x = 5
    y = 2.7172
    z = "cadenaPI"'''
    
    # # # # # # # MÉTODOS # # # # # # #
    # Constructor
    def __init__(self, xR = 0, yR = 0.0, zR = ""):
        self.x = xR
        self.y = yR
        self.z = zR    
    
    # Mostrar "string" de objeto
    def __str__(self):
        cadenaTMP =  "Valor de x: " + str(self.x)
        cadenaTMP += "\nValor de y: " + str(self.y)
        cadenaTMP += "\nValor de z: " + str(self.z)
        return cadenaTMP
    
    # Método nombreFuncion(unvalorentero)
    def nombreFuncion(self, valor = 666):
        print(f"El valor anterior de x es: {self.x}")
        self.x = valor
        print(f"El valor nuevo de x es: {self.x}")
    

# Instanciar un objeto
objeto1 = MiClase()

print(objeto1)

print(objeto1.x)

print(objeto1.nombreFuncion(10))

print(objeto1.nombreFuncion())

print(objeto1)

print("Esta es la cadena del objeto: \n" + str(objeto1))