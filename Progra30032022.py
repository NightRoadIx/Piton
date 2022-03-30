#%%

def saludar():
    print("Hola Dora la Exploradora")

def super_funcion(funcion):
    funcion()

funcion = saludar

# Ejecusización
super_funcion(funcion)



#%%

def funcion_a(funcion_b):
    def funcion_c():
        print('Antes de la ejecución de la función a decorar')
        funcion_b()
        print('Después de la ejecución de la función a decorar')

    return funcion_c

# Decorar la función saludar con la funcion_a
@funcion_a
def saludar():
    print("Salta Mario Bros 7.75 m")

# MAIN
saludar()


#%%

import time

# Decorador de interiores
# La función principal recibe un objeto funcion
def medirTiempo(fun):
    # La función interna recibe argumentos variables con
    # args y kwargs
    def wrapper(*args, **kwargs):
        # Vamos a comenzar a medir el tiempo
        inicio = time.time()
        # Aquí se ejecuta el objeto funcion y se asigan su posible resultado
        resultado = fun(*args, **kwargs)
        total = time.time() - inicio
        print("Se tardo: {} s".format(total))
        # Se regresa el resultado del objeto funcion
        return resultado
    # Se regresa la función interna
    return wrapper

# Función a decorar
@medirTiempo
def suma(a, b):
    time.sleep(1)
    return a + b

# Ejecutamos
print(suma(5, 3))