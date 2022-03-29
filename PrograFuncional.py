#%%
# PROGRAMACIÓN FUNCIONAL JAJAJAJAJA
def funcion(x, y, z):
    # CUERPO DE LA FUNCION
    w = x + y + z
    return w

# Parte de la función main
if __name__ == "__main__":
    
    # Invocar a la función
    print(funcion(1, 2, 3))
    
    # Funciones lambda
    # x(a) = f(a) = a + 10
    x = lambda a: a + 10
    
    # invocación de la función lambda
    print( x(5) )
    
    # y(r) = f(r) = r^2 + 1
    y = lambda r: r**2 + 1
    
    print( y(5) )
    
    # x2 = f(a, b) = a * b
    x2 = lambda a, b : a*b
    
    print( x2(5, 6) )
    
#%%
# FUNCIONES ANÓNIMAS
def miFuncion(n):
    # y = f(a) = a*n
    y = lambda a : a * n
    return y

'''
def miFuncion(n):
    def y(a):
        tmp = a * n
        return tmp
    return y
'''

duplicador = miFuncion(2)
# miFuncion(2, a):
#    return 2 * a
# duplicador = g(2) = g(f(a)) = 2*a

print( duplicador(11) )
print( duplicador(33) )

triplicador = miFuncion(3)

print( triplicador(11) )

#%%

def cuenta(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta(numero)
    else:
        print("Fin de los tiempos!!!!!! ")
    print("--FIN--", numero)


'''

etiqueta:
    INSTRUCCIONES
    ...
    JZ etiqueta2
    GOTO etiqueta

etiqueta2:
    INSTRUCCIONES
'''

#%%
def exponente(x, n):
    if n == 0:
        return 1
    else:
        return x * exponente(x, n-1)

'''
exponente(5, 3) =>      5*(5*(5*1))
 exponente(5, 3-1) =>     5*(5*1)
  exponente(5, 3-1-1) =>    5*1
   exponente(5, 3-1-1-1) =>  1
'''

#%%
def exponencialRapida(x, n):
    if n == 0:
        return 1
    elif n % 2 == 0:  # n es par
        return exponencialRapida(x*x, n/2)
    else:
        return x * exponencialRapida(x, n-1)

'''
eR(5, 4)
 eR(5*5, 4/2) => 5*5 * (5*5)
  eR(5*5, (4/2)/2) => 5*5
   eR(5, ((4/2)/2) - 1) => 1
'''

#%%
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89
def fib(n):
    if((n == 0) or (n == 1)):
        return 1
    else:
        return fib(n-1) + fib(n-2)

# Una función para el trazo de todas las llamadas a la serie
def trazar(f):
    # atributo del objeto f
    f.indent = 0
    def g(x):
        # obj.__str__ => comportamiento de cadena del obj
        # obj:__name__ => nombre del objeto como tal
        print('|  ' * f.indent + '|--', f.__name__, x)
        f.indent += 1
        # Aquí realizar todo lo que tiene que hacer la función f
        # valor = fib(x)
        valor = f(x)
        print('|  ' * f.indent + '|--', 'Regresar', repr(valor))
        f.indent -= 1
        return valor
    return g

# 
fib = trazar(fib)
print(fib(5))

#%%
# Memoización
cache = {}

def fib(n):
    # Revisar si n se encuentra en cache
    if n in cache:
        return cache[n]
    result = 0
    
    # Cache base
    if n <= 1:
        return n
    else:
        result = fib(n-1) + fib(n-2)
    cache[n] = result
    print(n, " - ", cache[n])
    
    return result

print( fib(50) )