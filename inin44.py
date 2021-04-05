'''
    Decoradores de funciones
    Es importante tomar en consideración lo siguiente para entender los 
    decoradores de funciones:
        1.- En Python, se puede definir una función dentro de otra
        2.- En Python, una función puede ser enviada como parámetro a otra
        función (incluso una función puede regresar otra función)
'''

#%%
# Por ejemplo, se crea una función con un mensaje de saludo
# la función recibe una cadena de texto
def mensaje(cadena):
    
    # Ahora se coloca una función al interior
    def saludar():
        return "Hola "
    
    # Ahora se regresa la concatenaciíon de la función y la cadena
    # (esto se puede realizar en otros lenguajes, pero llamando a las
    # funciones que, por supuesto, están definidas fuera de la función)
    return saludar() + cadena

# Se crea una función con el nombre
def perso(nombres):
    return nombres

# Se manda a llamar la función
print( mensaje(perso("Borola")) )

#%%
# Otra forma de realizar esto es asignando la función a una variable
variable = mensaje

print(variable("Borola"))

#%%
# Ahora bien, un decordor es una funciín que toma una función como parámetro
# y regresa una función. Esto es útil para "envolver" la funcionalidad
# con el mismo código una y otra vez.
# Se reescribirá el ejemplo anterior usando decoradores

def mensajeDcorado(fun):
    
    # Función anidado
    def saludar2(nombre):
        return "Hola " + fun(nombre)
    
    # La función regresa una función
    return saludar2

# Usar la notación @funcion para indicar que la siguiente función uilizará
    # la funcion especificada como decorador
@mensajeDcorado
def perso2(nombres2):
    return nombres2

# Aquí quiere decir que solo se utilzaá el nombre de la función que está decorada
# por otra
print(perso2("Borola"))

'''
    Como es que trabaja el decorador...
    1.-Se manda a llamar la función perso2() con un argumento
    2.-Esta función esta siendo decorada por otra (mensajeDcorado), por lo que
    se manda a llamar esta última función usando como argumento la función
    perso2()
    3.-Una vez dentro de la función hay otra, la cual recibe el argumento
    de la función perso2() y la propia función para mandarla a llamar
    y regresar el valor que se mando en un inicio "Borola"
    4.-Finalmente, la función decoradora regresa su función interna que 
    no es otra cosa que la concatenación de "Hola " + argumento de la función
    que originalmente se mando a llamar
'''


