import time
import math

# Función decorador para calulcar la duración que toma cualquier función en
# ejecutarse
def calcularTiempo(func):
    
    # En caso de que la función que se desea calcular el tiempo incluya
    # argumentos se puede utilizar como argumentos *args, **kwargs
    def calculo(*args, **kwargs):
        # Almacenar el tiempo antes de la ejecución
        inicio = time.time()
        
        # Ejecutar la función
        valor = func(*args, **kwargs)
        
        # Almacenar el tiempo al finalizar la ejecución
        fin = time.time()
        # Ahora imprimir, el atributo __name__ permite obtener el nombre 
        # de la función (recordad que Python al ser multiparadigma, usa
        # muchas cosas de la POO y las funciones son como tal objetos)
        print("Tiempo total que toma", func.__name__, "es", fin - inicio, "s")
        
        # La función regresará lo que la función de argumento regresa
        return valor
        
    # Regresar la función interna
    return calculo

# Se genera una función para calcular algun proceso y se le coloca la 
# la función decorador
@calcularTiempo
def factorial(num):
    # Hacer que la función se mantenga 2 segundos sin hacer nada, para que
    # se simule que la función tarda en ejecutarse
    time.sleep(2)
    # Regresa un valor
    return math.factorial(num)

# Llamar a la función
# Se debe recordar que se llamará también a la función decorador
print("{}! = {}".format(10, factorial(10)))