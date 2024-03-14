class Producto:
    def __init__(self, nombre, precio, marca, categoría):
        self.nombre = nombre
        self.precio = precio
        self.marca = marca
        self.categoría = categoría

    def getNombre(self):
        return self.nombre
    def getPrecio(self):
        return self.precio

class TV(Producto):
    def __init__(self, pulgadas, resolución):
        self.pulgadas = pulgadas
        self.resolución = resolución
    def getPulgadas(self):
        return self.pulgadas
    def getResolución(self):
        return self.resolución

mishi = Producto("Látex", 300, "Los del seguro", "Barrera")
print(mishi.getNombre())
pantallota = TV(72, "FullHD 4K")

# Agregar productos al carrito
carrito = []
carrito.append(pantallota)

# Calcular el total de compra
total = 0
for producto in carrito:
    total += producto.getPrecio()

# Mostrar el total
print("Total: " + total)