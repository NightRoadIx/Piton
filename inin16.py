'''
    ENCAPSULAMIENTO
    La técnica de encapsulación, es conocida como ocultación de datos, 
    le permite que los atributos de un objeto pueden ocultarse (superficialmente) 
    para que no sean accedidos desde fuera de la definición de una clase. 
    Para ello, es necesario nombrar los atributos con un 
    prefijo de doble subrayado: __
'''

class Factura:
    # Atributo encapsulado o privado
    __tasa = 16
    
    # Se genera el constructor
    def __init__(self, unidad, precio):
        self.unidad = unidad
        self.precio = precio
    
    # Método
    def porPagar(self):
        total = self.unidad * self.precio
        impuesto = total * Factura.__tasa / 100
        return (total + impuesto)
    
# MAIN
compra1 = Factura(12, 100)
print(compra1.unidad)
print(compra1.precio)
print(compra1.porPagar(), " pesos")

# LO SIGUIENTE PRODUCE UN ERROR
print("La tasa utilizada es: ", compra1.__tasa)

# En realidad lo que se tiene que hacer es lo siguiente
print("La tasa utilizada es: ", compra1._Factura__tasa)

# en general, solo los atributos se utilizan del tipo privado o encapsulado
# ya que en POO solo se necesita saber como interaccionr con los objetos 
# no se requiere conocer los detalles de como está implementada la clase