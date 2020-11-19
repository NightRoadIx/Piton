# # # # # # # MÓDULOS # # # # # # # 
# Importar módulo para graficación
import matplotlib.pyplot as plt
# Importar módulo para el uso de arreglos numéricos
import numpy as np
# Importar módulo para el uso de matemáticas simbólicas
import sympy as sp

    
# # # # # # # OBTENCIÓN DE ECUACIÓN # # # # # # # 
# Definición de la variable simbólica
# Ingresar que variable (en str) se va a utilizar como simbólica
# solo ingresar una letra o palabra simple (sin espacios)
while True:
    # Se obtiene la variable
    variable = input('Ingrese la variable: ')
    # Esto rompe cuando solo se usa un caracter sencillo o palabra como variable
    # lo que quiere decir que si en lo que se ingreso hay un espacio " "
    # Entonces no se puede continuar
    if (' ' in variable) == False:
        # Mostrar la variable
        print('La variable ingresada es: ', variable)
        # Romper el ciclo while
        break

# Lo siguiente es convertir esa str en una variable del tipo simbólica
# La transformación es de str a Symbol
x = sp.Symbol(variable)
# Ahora si, se ingresa la ecuación en formato str
equa = input('Ingresar la ecuación: ')
# TODO: *
# Aquí la restricción es extremadamente compleja, pues es posible que el usuario
# ingrese, técnicamente, cualquier cosa, por lo que se confiará en la buena
# fe del usuario
# Se "sympyfica" la cadena de texto ingresada, esto es que pasa a ser una
# variable del tipo "SYMPY"
y = sp.sympify(equa)

# # # # # # # MOSTRAR LOS DATOS INGRESADOS # # # # # # # 
# Se le muestra al usuario la gráfica de la función junto con la función
# Mostrar la función de forma "bonita"
print(y)
# Aquí se crea la etiqueta del eje y como f(variable)
ejey = 'f(' + variable + ')'
# Mostrar la gráfica
# sp.plotting.plot(y, xlabel = variable, ylabel = ejey)

# EN CASO DE QUE LA GRÁFICA CON SYMPY NO FUNCIONE
# Crear el intervalo de graficación
# TODO: Modificar que se muestre de manera automática
# un amplio intervalo para mostrar las posibles raíces
x1 = np.arange(-100,100,0.1) # 0, 0.1, 0.2, 0.3, 0.4 ... 19.9
# Generar una lista con las evaluaciones de la función
''' Esto es muy similar a utilizar lo siguiente:
    y1 = []
    for tmp in x1:
        y1.append(float(y.subs(x,tmp).evalf()))
    Pero en una sola línea
'''
y1 = [float(y.subs(x,tmp).evalf()) for tmp in x1]
# Una vez realizado esto, mostrar la gráfica
plt.plot(x1, y1)
plt.xlabel(variable)
plt.ylabel(ejey)
plt.grid()
plt.show()

#%%
# # # # # # # INGRESAR EL INTERVALO DE BÚSQUEDA # # # # # # # 
# Una vez que ya se tiene la gráfica, entonces el usuario ya es capaz de
# decidir el intervalo donde se iniciará la búsqueda
while True:
    # Pedir los valores de [a, b] [xl, xu]
    a = float(input('Ingresar límite inferior a: '))
    b = float(input('Ingresar límite superior b (> a): '))
    # Verificar que a < b y además f(a)f(b) < 0 (esto es, hay una raíz
    # entre los límites colocados)
    if (a < b) and ( (float(y.subs(x,a).evalf())*float(y.subs(x,b).evalf())) < 0 ):
        break

# Gurdar los límites iniciales
a0, b0 = a, b

# # # # # # # INGRESAR LOS DIGITOS DE PRECISIÓN # # # # # # # 
# Ahora pedir la cantidad de dígitos de precisión
while True:
    d = int(input('Ingresar los dígitos de precisión (> 0): '))
    # Verificar que son más de 1 dígito de precisión
    if d > 0:
        break
# Calcular el error mínimo a partir del dígito de precisión
epsilon = float(1 / (10**d))

# # # # # # # INGRESAR EL NOMBRE DEL ARCHIVO # # # # # # # 
# Ingresar el nombre del archivo a almacenar
archon = input("Ingresar el nombre del archivo a guardar: ")
# Generar el nombre con extensión
archon += '.txt'
# Abrir el archivo para escritura
f = open(archon, "w")
# Colocar el encabezado del archivo
f.write("--Método de bisección--\n")
f.write("Ecuación: " + equa + "\n")
f.write("Intervalo de búsqueda: [{:},{:}]\n".format(a, b))
f.write("Precisión: {:}\n".format(d))

# # # # # # # PROGRAMA PRINCIPAL # # # # # # # 
# Obtener el parámetro h 
h = (b-a) / 2.0
# Un contador para las repeticiones del método
i = 1
mant = 1

# APLICACIÓN DEL MÉTODO #
# Se coloca un encabezado
print("{:12}\t{:12}\t{:12}\t{:12}\t{:12}".format('i','a','b','m','h'))
while(h > epsilon):
    # Se halla m (el punto intermedio, el cual bisecciona el intervalo)
    m = (a+b) / 2
    # m = float(b - ( ( y.subs(x,b).evalf() * (a-b) )/(y.subs(x,a).evalf() - y.subs(x,b).evalf() ) ))    
    # Generar un texto que es cada fila en de la tabla, la cual representa
    # cada una de las iteraciones
    testo = "{:}\t{:12}\t{:12}\t{:12}\t{:12}".format(i,round(a,d),round(b,d),round(m,d),round(h,d))
    # Mostrarlo en pantalla
    print(testo)
    # Escribir en el archivo
    f.write(testo+"\n")
    # Ahora determinar el nuevo intervalo
    # ...En este caso para hallar el valor de f(a) por ejemplo, se debe usar
    # ...el método subs(x,a) para la ecuación guardada en y, además de también
    # ...utilizar el método evalf() y además para avitar problemas, utilizar
    # ...la función integrada float() para convertir a tipo flotante
    # En caso de que f(a)f(m) < 0
    if( float(y.subs(x,a).evalf())*float(y.subs(x,m).evalf()) < 0):
        # a se mantiene & b pasa a ser m
        b = m
    # En caso de que f(m)f(b) < 0        
    elif( float(y.subs(x,m).evalf())*float(y.subs(x,b).evalf()) < 0):
        # a ahora será m & b se mantiene
        a = m
    #h = (b - a) / 2
    if i > 1:
        h = abs((m-mant)/m)
    i += 1
    mant = m

# # # # # # # RESULTADOS # # # # # # # 
print("La raíz a {:} dígitos de precisión es: {:}".format(d, round(m,d)))
f.write("La raíz a {:} dígitos de precisión es: {:}".format(d, round(m,d)))
sp.plotting.plot(y, (x, a0, b0), xlabel = variable, ylabel = ejey)
f.close() # IMPORTANTE CERRAR EL ARCHIVO