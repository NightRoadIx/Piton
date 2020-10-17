'''
    MANEJO DE EXCEPCIONES
    El manejo de exepciones permite controlar los errores de un programa en tiempo de ejecución .
    Generalmente, cuando un error ocurre (división entre 0, operar variables de tipos diferentes)
    el programa normalmente se detiene y genera un mensaje de error.
    El término técnico para esto es que el programa lanza una excepción (o arroja un error).
    		
    Para esto se utiliza la instrucción try-except-else-finally
'''

#%%
a = 5 / 0

#%%

#x = 5
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

#%%

# Puede ocurrir una excepción cuando se realiza una división entre 0
def divide(x, y):
    try:
        # Se realiza la división
        resultado = x // y
    except ZeroDivisionError:
        print("Error, no se puede dividir entre 0")
    else:
        print("Resultado es : " + str(resultado))

divide(5,0)
print("Sin embargo, el programa sigue")

#%%
# También es posible que se genere un error al intentar ingresar
# a un elemento inexistente en una lista
a = [1, 2, 3]
try:
    print("El segundo elemento {:}".format(a[1]))
    # Esto generará un error
    print("El cuarto elemento {:}".format(a[3]))
except IndexError:
    print("Se intento ingresar a un índice no válido")
finally:
    print("Siempre se ejecuta")

#%%

# En ocasiones también es necesario el manejo de dos o más
# excepciones
try:
    a = 3
    if a < 4:
        # Lanzar una excepción ZeroDivisionError
        b = a / (a - 3)
    # Esto lanza otra excepción NameError
    print("Valor de b: ", b)
except (ZeroDivisionError, NameError):
    print("Un error sucedio y fue controlado")

print("Sin embargo, el programa sigue")
