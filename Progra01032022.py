class MiClase:
    # # # # # # # ATRIBUTOS # # # # # # #
    '''x = 5       # HARCODEEEEE!!!!
    y = 2.7172
    z = "cadenaPI"'''
    __varia = 16  # soy especial!
    
    # # # # # # # MÉTODOS # # # # # # #
    # Constructor
    # this = self
    def __init__(self, xR = 0, yR = 0.0, zR = ""):
        self.x = xR
        self.y = yR
        self.z = zR
    
    # Mostrar "string" de objeto
    def __str__(self):
        cadenaTMP =  "Valor de x: " + str(self.x)
        cadenaTMP += "\nValor de y: " + str(self.y)
        cadenaTMP += "\nValor de z: " + str(self.z)
        # Regresar siempre una cadena de texto
        return cadenaTMP
    
    # Método nombreFuncion(unvalorentero)
    def nombreFuncion(self, valor = 666):
        print(f"El valor anterior de x es: {self.x}")
        self.x = valor
        print(f"El valor nuevo de x es: {self.x}")

# Instanciar un objeto
objeto1 = MiClase()

# Aquí se observa el comportamiento del objeto como cadena (__str__)
print(objeto1)

print(objeto1.x)

print(objeto1.nombreFuncion(10))

print(objeto1.nombreFuncion())

print("Esta es la cadena del objeto: \n" + str(objeto1))

# Imprimir variable encapsulada
print(objeto1._MiClase__varia)