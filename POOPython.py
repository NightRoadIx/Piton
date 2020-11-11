# -*- encoding: utf-8 -*-

# Clase figura, que es la clase padre
class Figura:
    # # # # Atributos # # #
    perimetro = 0.0
    area = 0.0
    
    # # # # Metodos (Funciones) # # #
    def imprimirValores(self):
        return "\nPerimetro: {:}\nArea      : {:}\n".format(self.perimetro, self.area)

# Clase cuadrado
# Hereda de la clase Figura
class Cuadrado(Figura):
    # # # # Atributos # # #
    lado = 0.0
    color = ""
    
    # # # # Metodos (Funciones) # # #
    # Metodos especiales
    # Constructor
    def __init__(self, lonLado):
        # Se asigna el valor de inicio del constructor
        self.lado = lonLado
    
    # Metodo para mostrar datos en formato string
    # De los atributos que se deseen
    def __str__(self):
        cadena = "--\nCuadro {:} x {:}".format(
                self.lado, self.lado) + self.imprimirValores() + "--\n"
        return cadena
    # Método para el cálculo del perímetro
    def calcularPerimetro(self):
        self.perimetro = self.lado * 4.0
    # Método para el cálculo del área
    def calcularArea(self):
        self.area = self.lado**2

# Clase rectangulo
# Hereda de la clase Figura
class Rectangulo(Figura):
    # # # # Atributos # # #
    base = 0.0
    altura = 0.0
    color = ""
    
    # # # # Metodos (Funciones) # # #
    # Metodos especiales
    # Constructor
    def __init__(self, lonBase, lonAltura):
        # Se asigna el valor de inicio del constructor
        self.lado = lonBase
        self.altura = lonAltura
    
    # Metodo para mostrar datos en formato string
    # De los atributos que se deseen
    def __str__(self):
        cadena = "--\nRectangulo {:} x {:}".format(
                self.base, self.altura) + self.imprimirValores() + "--\n"
        return cadena
    # Método para el cálculo del perímetro
    def calcularPerimetro(self):
        self.perimetro = (self.base + self.altura) * 2.0
    # Método para el cálculo del área
    def calcularArea(self):
        self.area = self.base * self.altura
     
# # # # MAIN # # #
if __name__ == "__main__":
    # Aqui se instancia con el constructor
    cuadro01 = Cuadrado(4)
    cuadro02 = Cuadrado(8)
    rectangulo01 = Rectangulo(5, 4)
    
    cuadro01.calcularArea()
    cuadro01.calcularPerimetro()
    
    rectangulo01.calcularPerimetro()
    rectangulo01.calcularArea()
    
    print(cuadro01)