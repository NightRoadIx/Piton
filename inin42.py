'''
    COMPLEJIDAD COMPUTACIONAL
    La complejidad computacional es una materia altamente venerable en 
    Ciencias de la Computación. Puede ser definida como la cantidad de 
    tiempo y espacio que el algoritmo requiere para resolver un problema.
    
    De esta forma, también se considera que existen problemas que al
    ser analizados bajo la complejidad computacional, son "intratables";
    esto no quiere indicar que sean imposibles de resolver, sin embargo,
    indica que no hay algoritmos que pueden resolver este tipo de problemas
    de forma eficiente (con un uso de memoria adecuado y en tiempo razonable)
    
    Una de las formas en las que se analiza la complejidad computacional
    es el peor de los escenarios. 
    La variable independiene sería el tamaño de entrada de los datos, 
    y el ritmo de crecimiento de datos es la variable dependiente, y se realiza
    el análisis cuando este crecimiento de datos tiende a infinito. 
    Este análisis se le conoce como big-Oh.
'''
import numpy as np 
import matplotlib.pyplot as plt 
  
# Función que calcula x ^ n para un n dado
def poly(n): 
    def polyXN(x): 
        return x**n 
    return polyXN 

# En este programa se compararán ciertas funciones matemáticas:
# logaritmo natural, función lineal, funció cuadrada, función cúbica y exponencial (e)

# Las fuciones a comparar se colocan en una lista
FUNCTIONS = [np.log, poly(1), poly(2), poly(3), np.exp] 
# y se colocan también los colores
COLORS = ['c', 'b', 'm', 'y', 'r'] 
  
# Graficar
def compareAsymptotic(n): 
    # Se obtiene un arreglo de 1 a n
    x = np.arange(1, n, 1)
    plt.title('O(n) para n =' + str(n)) 
    # Se juntan ambnas listas y se itera sobre ellas para graficar
    for f, c in zip(FUNCTIONS, COLORS): 
        plt.plot(x, f(x), c)
    plt.legend(['ln(x)','x','x^2','x^3','exp(x)'])
    # Mostrar la gráfica
    plt.show() 
          
# Mostrar como crece la complejidad computacional 
    # de acuerdo al número n de entrada
compareAsymptotic(3) 
compareAsymptotic(5) 
compareAsymptotic(10) 
compareAsymptotic(20) 