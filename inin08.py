'''
    MANEJO DE EXCEPCIONES
    El manejo de exepciones permite controlar los errores de un programa en tiempo de ejecución .
    Generalmente, cuando un error ocurre (división entre 0, operar variables de tipos diferentes)
    el programa normalmente se detiene y genera un mensaje de error.
    El término técnico para esto es que el programa lanza una excepción (o arroja un error).
    		
    Para esto se utiliza la instrucción try-except-else-finally
'''

try:
    # La variable x no esta definida, entonces esto produce un error en tiempo de ejecución
    print(x)
except:
    # Se muestra cuando ocurre la excepción
    print("Ha ocurrido una excepción")
else:
    # No ocurre la excepción
    print("No exisitió ninguna excepción")
finally:
    # Esto se ejecuta siempre, exista o no una excepción
    print("El bloque try - except termino")


# Puede ocurrir una excepción cuando se realiz auna división entre 0
def divide(x, y):
    try:
        # Se realiza la división
        resultado = x // y
    except:
        print("Error, no se puede dividir entre 0")
    else:
        print("Resultado es : " + str(resultado))

divide(5,0)
