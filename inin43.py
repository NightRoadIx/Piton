'''
    *ARGS, **KWARGS en Python
    La sintaxis especial *args en la definición de funciones es utilizada para
    pasar un número variable de argumentos a una función. 
    Es utilizado para pasar argumentos sin palabras clave (variables),
    esto es una lista de argumentos variables
    
    Esta notación proviene desde C, el cual permitía mandar argumentos
    variables cuando el programa se ejecuta, aún se puede osbervar esto,
    por ejemplo cuando se ejecuta la instrucción 'pip' para instalar
    librerías en Python, ya que el programa se llama pip, pero se ejecuta
    con los argumentos:
        pip install ALGO
    
    Por tanto, esta es la reminiscencia de los apuntadores
    *  -> algo similar a un arreglo
    ** -> algo similar a una arreglo de arreglos (matriz)
'''
def miFuncion(*args, **kwargs):
    print("args: ", args)
    print("kwargs: ", kwargs)

# Ahora se pasan los argumentos y sus valores en la función
# pueden ser de cualquier longitud
miFuncion("Helden", "David", "Bowie", primer = 666, segundo = "Heroes")
# ¿Qué regresa esta función?