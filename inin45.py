# Declaración de la función decorador
def decorador(*args, **kwargs):
    # Impresión de un texto dentro del decorador
    print("Dentro del decorador")
    
    # Función interna del decorador
    def interna(func):
        # Imprimir algo
        print("Dentro de la función interna del decorador")
        # Imprimir un mensaje mandando a llamar el arguento recibido 
        # con el identificador de variable "gusto"
        print("Me gusta", kwargs['gusto'])
        
        # Mandar a llamar la función a decorar
        func()
    
    # Regresar la función interna
    return interna

# Usar el decorador con un argumento
@decorador(gusto = "Rey Julien")
def miFuncion():
    print("Dentro de la función actual")

# en este caso, la función se ejecuta de manera automática