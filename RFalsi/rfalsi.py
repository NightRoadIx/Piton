import sympy as sp
import metodo1 as rf

# MAIN 
x = sp.Symbol('x')
f = 4 * sp.sin(x) - 3*x
sp.pretty_print(f)
sp.plotting.plot(f)

while True:
    a = float(input('Ingresa el valor del limite inferior -> '))
    b = float(input('Ingresa el valor del limite superior -> '))
    if(a < b): break
    print('Valores erróneos, a no puede ser mayor que b')

aant = a
bant = b

d = float(input('Ingresa los dígitos de precisión     -> '))
e = 1 / (10**d)

m = rf.regulafal(f, x, a, b, e)

print("La raíz es: {}".format( round(m,int(d)) ))
sp.plotting.plot(f, (x, aant, bant))