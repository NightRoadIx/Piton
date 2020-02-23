'''
	Uso de las librerías sympy
	Los cuales permiten manejar matemáticas simbólicas
'''
# Importar las librerias
import sympy as sym

# Esto es para mostrar una división
a = sym.Rational(1, 2)
# pero esto es una fracción simbólica
print(a)

# Esto genera pi al cuadrado
print(sym.pi**2)

# Sin embargo, el tipo de dato es simbólico, por lo que se tiene que utilizar
# el método evalf() para obtener el valor numérico de la evaluación
print( (sym.pi**2).evalf() )


# Uso de símbolos
# Para agenerar variables simbólicas, se tiene que asiganr estas variables
# utilizando el método Symbolic()
x = sym.Symbol('x')
y = sym.Symbol('y')

# y ya se puede manipular
print(x + y + x - y)

# Realizar expansión de una función
print(sym.expand((x+y)**3))

# Mnadar a que se expanda de forma trigonométrica
print(sym.expand(sym.cos(x + y), trig=True))

# O realizar la simplificación
print(sym.simplify((x + x * y) / x))


# Graficación
# Mantener la grafica sin mostrar
g1 = sym.plotting.plot(x*x, show=False)
g2 = sym.plotting.plot(x, show=False)
# Añadir la gráfica g2 en la g1
g1.append(g2[0])
# Ahora si mostrar
g1.show()

# Grafiación de funciones paramétricas
# Generar el símbolo
u = sym.Symbol('u')
sym.plotting.plot_parametric(sym.cos(u), sym.sin(u), (u, -5, 5))


# Grafiación en 3D
sym.plotting.plot3d(x*y, (x, -5, 5), (y, -5, 5))
# Inlcuso graficar varias funciones con diferentes intervalos
sym.plotting.plot3d((x**2 + y**2, (x, -5, 5), (y, -5, 5)),
    (x*y, (x, -3, 3), (y, -3, 3)))

# grafiación de funciones paramétricas en 3D
sym.plotting.plot3d_parametric_line(sym.cos(u), sym.sin(u), u, (u, -10, 10))

# Evaluación de límites
print(sym.limit(sym.sin(x) / x, x, 0))
# calcular en infinito
print(sym.limit(x, x, sym.oo))


# Obtener las derivadas
sym.diff(sym.sin(x), x)

# Usar:
#  init_printing(use_unicode=True)
# permite mostrar de forma más "bonita" la forma simbólica
# Otra forma es usar
#  sym.pretty()

# Derivadas parciales
z = sym.Symbol('z')
# Función
expr = sym.exp(x*y*z)

# si se desea la parcial de x, la segunda parcial de y y la parcial de z
print(sym.diff(expr, x, y, y, z))


# Integración
print( sym.pretty(sym.integrate(6 * x**5, x)) )
# Por supuesto, es posible hallar la intergal definida
print( sym.integrate(x**3, (x, -1, 1)) )

# Incluso las intergales impropias
print( sym.pretty(sym.integrate(sym.exp(-x ** 2), (x, -sym.oo, sym.oo))) )

# Ecuaciones diferenciales
# Generar los símbolos como funciones
f, g = sym.symbols('f g', cls=sym.Function)

# Ahora f & g son funciones indefinidas
print(f(x))
# Ahora crear la ecuación diferencial
print( sym.pretty(f(x).diff(x, x) + f(x)) )

# resolver la ecuación diferencial
print( sym.pretty(sym.dsolve( f(x).diff(x, x) + f(x) )) )

