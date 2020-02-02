# Obtener el número por el dispositivo de entrada de default
n = int(input("Numero a conocer la tabla: "))

# Recorrer del 1 al 10
for k in range(1,11):
    # Mostrar la tabla con 4 espacios asignados a cada número
    print("{:4d} x {:4d} = {:4d}".format(n, k, n*k))