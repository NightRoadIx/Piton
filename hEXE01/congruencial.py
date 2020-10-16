# Generador de números congruencial

# Ingresar los parámetros a, b, m
# TODO: Como verificar que lo que ingresa el usuario es un entero?
a = int(input('Ingrese el valor del multiplicador a    : '))
b = int(input('Ingrese el valor del sesgo b            : '))
m = int(input('Ingrese el valor del módulo m           : '))

# Ingresar el valor de números a obtener
N = int(input('Ingrese la cantidad de datos a obtener N: '))

# Iniciar el contador a 0
n = 0

# Generar un número semilla en una lista
# TODO: También el usuario debería iniciar un número semilla
X = [5]
# Números aleatorios
U = []

print('{:6}\t{:6}\t{:12}\t\t{:12}'.format('n','Xn','Xn+1 = (aXn + b)mod m','Un = Xn/m'))
while n <= N:
    # Obtener el número aleatorio
    U.append(X[n] / m)
    # Crear el nuevo número semilla
    X.append( (a*X[n] + b) % m )
    
    # Colocar una tabla con los valores
    print('{:}\t{:2}\t({:}*{:} + {:}) mod {:} = {:}\t{:14}'.format(n,X[n],a,X[n],b,m,X[n+1],round(U[n],4)))
    # Incrementar el contador
    n += 1