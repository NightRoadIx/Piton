#%%
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

# Definición de la variable simbólica
# Ingresar que variable se va a utilizar como simbólica
# solo ingresar una letra o palabra simple (sin espacios)
while True:
    variable = input('Ingrese la variable: ')
    # Esto rompe cuando solo se usa un caracter sencillo o palabra como variable
    if (' ' in variable) == False:
        break
# La convertimos en variable simbólica (de cadena pasa a simbólica con Symbol)
x = sp.Symbol(variable)
# Ahora si, se ingresa la ecuación
equa = input('Ingresar la ecuación: ')
# Aquí la restricción es extremadamente compleja, pues es posible que el usuario
# ingrese, técnicamente, cualquier cosa, por lo que se confiará en la buena
# fe del usuario
# Se "sympyfica" la cadena de texto ingresada
y = sp.sympify(equa)

# Se le muestra al usuario la gráfica de la función con su función ingresada
sp.pretty_print(y)
ejey = 'f(' + variable + ')'
sp.plotting.plot(y, xlabel = variable, ylabel = ejey)

# Con la gráfica, entonces ya se pueden colocar los límites en donde buscar
# las raíces
while True:
    a= float(input('Ingresar límite inferior a: '))
    b= float(input('Ingresar límite inferior b (> a): '))
    # Verificar que a < b y además f(a)f(b) < 0 (esto es, hay una raíz
    # entre los límites colocados)
    if (a < b) and ( (float(y.subs(x,a).evalf())*float(y.subs(x,b).evalf())) < 0 ):
        break

# Gurdar los límites iniciales
a0, b0 = a, b

# Ahora pedir la cantidad de dígitos de precisión
while True:
    d = int(input('Ingresar los dígitos de precisión (> 0): '))
    if d > 0:
        break
# Calcular el error mínimo
epsilon = float(1 / (10**d))

# Ingresar el nombre del archivo a almacenar
archon = input("Ingresar el nombre del archivo a guardar: ")
# Generar el nombre con extensión
archon += '.txt'
# Abrir el archivo para escritura
f = open(archon, "w")
# Colocar el encabezado
f.write("--Método de bisección--\n")
f.write("Ecuación: " + equa + "\n")
f.write("Intervalo de búsqueda: [{:},{:}]\n".format(a, b))
f.write("Precisión: {:}\n".format(d))

# Programa principal
h = (b-a) / 2.0
i = 1

# Método en sí
print("{:12}\t{:12}\t{:12}\t{:12}\t{:12}".format('i','a','b','m','h'))
while(h > epsilon):
    m = (a+b) / 2
    testo = "{:}\t{:12}\t{:12}\t{:12}\t{:12}".format(i,round(a,d),round(b,d),round(m,d),round(h,d))
    print(testo)
    f.write(testo+"\n")
    if( float(y.subs(x,a).evalf())*float(y.subs(x,m).evalf()) < 0):
        a = a
        b = m
    elif( float(y.subs(x,m).evalf())*float(y.subs(x,b).evalf()) < 0):
        a = m
        b = b
    h=(b-a) / 2
    i += 1

print("La raíz a {:} dígitos de precisión es: {:}".format(d, round(m,d)))
f.write("La raíz a {:} dígitos de precisión es: {:}".format(d, round(m,d)))
sp.plotting.plot(y, (x, a0, b0), xlabel = variable, ylabel = ejey)
f.close()