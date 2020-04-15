'''
    Multithreading (multihilos)
    En computación, un proceso es una instancia de un programa computacional 
    el cual está siendo ejecutado. Cualquier proceso tiene 3 componentes básicos:
        * Un programa ejecutable
        * Los datos asociados al programa (variables, buffers, etc.)
        * El estado del proceso
    Un hilo es una entidad dentro de un proceso que puede ser programada
    para su ejecución. También, es la menor unidad de procesamiento
    que puede ser ejecutada en un Sistema Operativo (OS)
    
    En palabras simples, un hilo es una secuencia de instrucciones detro de
    un programa que pueden ser ejecutadas de manera independiente de otro código
    Un hilo cuenta con la siguiente información:
        * Identificador del hilo, el nombre del hilo
        * Apuntador de la pila, es un apuntador a las variables que se usan
          en el hilo
        * Contador de programa, lleva el registro de que instrucción se está
          ejecutando
        * Estado del  hilo, en ejecución, esperando, iniciando, finalizado
        * entro otros
    
    En un solo proceso es posible que existan diferentes hilos, los cuales
    se pueden ejecutar al mismo tiempo.
'''
# importar la librería para el manejo de hilos
import threading

# Crear una función para obtener e imprimir el cubo de un número
def print_cubo(num):
    print("Cubo: {}".format(num**3))

# Crear una función para obtener e imprimir el cuadrado de un número
def print_cuad(num):
    print("Cuadrado: {}".format(num**2))

#
# Crear los hilos (se instancia un objeto con su constructor)
# el argumento del constructor es la función a ejecutar 
    # y los datos que recibe dicha función (en caso de que así sea)
t1 = threading.Thread(target = print_cuad, args=(10,))
t2 = threading.Thread(target = print_cubo, args=(10,))

# Comenzar con el hilo 1
t1.start()
# comenzar el hilo 2
t2.start()

# esperar hasta que el hilo 1 se haya ejecutado completamente
t1.join()
# esperar hasta que el hilo 2 se haya ejecutado completamente
t2.join()
# esto es importante para detener la ejecución de los hilos

print('Listo!')