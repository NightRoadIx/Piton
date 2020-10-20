# Generador de números congruencial
#%%
# Función para revisar que se trata de un valor positivo
def ingresarIntPositivo(numero):
    return numero >= 0

# Función para permitir el ingreso de solo valores enteros
# Se incluye un valor por defecto
def ingresarInt(mensaje = "Ingresa un valor entero: "):
    # Ingresar a un ciclo infinito
    while True:
        # La respuesta se recibe con un input y el mensaje enviado como argumento
        resp = input(mensaje)
        # Se ingresa a una sección try-catch
        try:
            # En este caso se intenta convertir a un valor entero (int)
            valor = int(resp)
            # Revisar si es un valor positivo
            if ingresarIntPositivo(valor):
                break
            print("No es un valor positivo")
        # Aquí se maneja la excepción
        except ValueError:
            # Se muestra un letrero de que se ingrese de nuevo un valor
            print("El valor no es un número entero")
            print("Favor de ingresar de nuevo")
    # Una vez que se salga del ciclo, se regresa el valor
    return valor

#%%
# Ingresar los parámetros a, b, m
a = ingresarInt('Ingrese el valor del multiplicador a    : ')
b = ingresarInt('Ingrese el valor del sesgo b            : ')
m = ingresarInt('Ingrese el valor del módulo m           : ')

# Ingresar el valor de números a obtener
N = ingresarInt('Ingrese la cantidad de datos a obtener N: ')

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
