'''
	Uso de las librerías numpy y matplotlib
	Estas librería agregan mayor soporte para el uso de
	vextores y matrices
'''
# Importar las librerias
import numpy as np
import matplotlib.pyplot as plt

# Crear una vector de o a 2Pi con 100 elementos en el intervalo
x = np.linspace(0, 2 * numpy.pi, 100)
# Función seno en numpy
y = np.sin(x)

# Graficar utilizando Matplotlib
# La librería permite hacer modificaciones a las gráficas
plt.plot(x, y, "-", linewidth=3, color = (0.2, 0.1, 0.4))
plt.title("Grafica x - y")
plt.grid()
plt.show()


''' Uso de arreglos '''
# arange es muy similar a range(), pero utilizando valores reales
# el uso de reshape() permite modificar el arreglo de números
# a una matriz de (3,5) en este caso
a = np.arange(15).reshape(3,5)

print(a)

# La función o método shape proporciona el tamaño del arreglo
print(a.shape)
# la propiedad ndim, permite conocer las dimensiones del arreglo
print(a.ndim)
# el tamaño total de elementos
print(a.size)


# Otra forma de crear arreglos es mediante
a = np.array([1, 2, 3, 4])

# crear un arreglo bidimensional 3x4 de ceros
zeros = np.zeros( (3,4) )
print(zeros)

# o de unos...
unos = np.ones( (2,3) )
print(unos)

# Matriz identidad
d = np.eye(3)
print(d)

# Valores aleatorios
e = np.random.random([2,2])
print(e)



a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(a)
# Se puede obtener un "pedazo" de la matriz mediante:
print(a[:2, 1:3])
# Si esta submatriz se asigna a una variable
b = a[:2, 1:3]
# y se hace la modificación de un elemento de la submatriz
b[0,0] = 77
# modifica el elemento de la matriz original también
print(a)


# se vuelve a generar el arreglo
a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# Obtenemos todos los elementos de la primer columna
col_r1 = a[:,1]
# Esto es obtener los elementos de la primer columna
col_r2 = a[:, 1:2]
# Ahora observar la diferencia de lo que se obtiene
print(col_r1, col_r1.shape)
print(col_r2, col_r2.shape)


a = np.array([[1,2], [3, 4], [5, 6]])
# Se puede obtener un nuevo elemento al hacer un indexado
# de la siguiente forma
print(a[[0, 1, 2], [0, 1, 0]])  # Prints "[1 4 5]"
# Se toman los elementos [0,0] [1,1] [2,0]
# Lo cual se puede observar de la siguiente forma
print(np.array([a[0, 0], a[1, 1], a[2, 0]]))  # Prints "[1 4 5]"

# Se puede encontrar valores que cumplan cierta condición
# Regresaun arreglo con los valores que cumplan esta condición
print( a[a > 2] )

# El método dtype regresa el tipo de datos del arreglo
print( a.dtype )


# Generar nuevos areglos del tipo flotante de 64 bits
x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)

# Suma de arreglos
print(x + y)
print(np.add(x, y))

# Diferencia de arreglos
print(x - y)
print(np.subtract(x, y))

# Multiplicación de arreglos (elemento a elemento)
print(x * y)
print(np.multiply(x, y))

# División de arreglos
print(x / y)
print(np.divide(x, y))

# Raíz cuadrada de arreglos
print(np.sqrt(x))

v = np.array([9,10])
w = np.array([11, 12])

# Lo siguiente genera el producto interior (punto)
print(v.dot(w))
print(np.dot(v, w))


# Suma de los elementos de un arreglo
print(np.sum(x))
# suma de los elementos de las columnas
print(np.sum(x, axis=0))
# suma de los elementos de las filas
print(np.sum(x, axis=1))


# Traspuesta de una matriz
print(x.T)


# Distancia entre dos puntos
# Se incluye
from scipy.spatial.distance import pdist, squareform
x = np.array([[0, 1], [1, 0], [2, 0]])
print(x)

# Ahora se encuentra la distancia Euclídea 
# entre todas las filas del vector x
d = squareform(pdist(x, 'euclidean'))
print(d)


# # # # # # GRAFICACIÓN 
# Generar las coordenadas (x,y) para los puntos
x = np.arange(0, 3 * np.pi, 0.1)
# del seno()
y = np.sin(x)

# Graficar (generar la gráfica)
plt.plot(x, y)
# Mostrar la gráfica
plt.show()


# Generar las coordenadas (x,y) para los puntos
x = np.arange(0, 3 * np.pi, 0.1)
# Generar dos ecuaciones a graficar
y_sin = np.sin(x)
y_cos = np.cos(x)

# Graficar la primera ecuación
plt.plot(x, y_sin)
# Graficar la segunda ecuación
plt.plot(x, y_cos)
# Rejilla
plt.grid()
# Texto que se coloca en el eje x
plt.xlabel('Eje x')
# Texto que se coloca en el eje y
plt.ylabel('Eje y')
# Título de la gráfica
plt.title('Seno y Coseno')
# Leyenda 
plt.legend(['Seno', 'Coseno'])
plt.show()


# Generar subplots
# Crear el subplot de 2 filas y 1 columna, posición 1
plt.subplot(2, 1, 1)
# Genera la primera gráfica
plt.plot(x, y_sin)
plt.title('Seno')

# Ahora va el segundo subplot
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Coseno')

# Mostrar la figura
plt.show()


# Gráficas de barras
# generar una figura del matplotlib
fig = plt.figure()
# Y se crean los ejes en donde se van a colocar
ax = fig.add_axes([0,0,1,1])
# Los valores que se colocarán en el eje x
leng = ['C', 'C++', 'C#', 'Python', 'Rust']
# Los valores del eje y
estudiando = [23, 17, 35, 29, 12]
# Generar la gráfica de barras
ax.bar(leng, estudiando)
plt.show()

# Gráfica de pastel
# generar una figura del matplotlib
fig = plt.figure()
# Y se crean los ejes en donde se van a colocar
ax = fig.add_axes([0,0,1,1])
# ejes iguales
ax.axis('equal')
# Los valores que se colocarán en el eje x
leng = ['C', 'C++', 'C#', 'Python', 'Rust']
# Los valores del eje y
estudiando = [23, 17, 35, 29, 12]
# Crear la gráfica
ax.pie(estudiando, labels = leng, autopct='%1.2f%%')
plt.show()

# Generar histogramas
# Se generarán datos con una distibución del tipo gaussiano
mu, sigma = 100, 15
# Crear un arreglo numpy con la distribución gaussiana, generando 10,000 números aleatorios
x = mu + sigma * np.random.rand(10000)

# Se genera en tonces los datos para el histograma
# hist
# Recibe: arreglo numpy con los datos, cantidad de barras a generar, densidad para normalizar el histograma, color, transparencia de color
# Regresa: arreglo o lista de arreglos con los valores de cada barra, el borde de las barras, lista de parches individuales usados para crear el histograma
n, bins, patches = plt.hist(x, 50, density = True, facecolor = 'g', alpha = 0.75)

# Arreglar el histograma
plt.xlabel('Valores')
plt.ylabel('Probabilidad')
plt.title('Histograma')
plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()

# Mapas de vectores
# quiver(x, y, u, v)
# coordenadas x, coordenadas y, magnitud en x de los vectores, magnitud en y de los vectores
# se generan los puntos en (x, y) como una especie de rejilla que va de [-2, 2] con pasos de 0.2
x,y = np.meshgrid(np.arange(-2, 2, .2), np.arange(-2, 2, .25))
# Esta es la función vectorial z = x e^(x^2 - y^2)
z = x*np.exp(-x**2 - y**2)
# esto regresa el gradiente de un arreglo N-dimensional
v, u = np.gradient(z, .2, .2)
# Esto genera la figura y los ejes
fig, ax = plt.subplots()
q = ax.quiver(x,y,u,v)
plt.grid()
plt.show()


# GRAFICACIÓN EN 3D
# Debe importarse el siguiente toolkit
from mpl_toolkits import mplot3d
# Crear la figura
fig = plt.figure()
# Crear los ejes, con proyección 3D
ax = plt.axes(projection='3d')
# Se genera un arreglo numpy que va de 0 a 100 con pasos de 1
z = np.linspace(0, 1, 100)
# la ecuación paramétrica es:
#  x = z * sin(20z)
x = z * np.sin(20 * z)
# y = z * cos(20z)
y = z * np.cos(20 * z)
ax.plot3D(x, y, z, 'gray')
ax.set_title('Gráfica 3D lineal')
plt.show()

# Gráfica de superficie 3D
# Se genera el producto exterior de 2 vectores
x = np.outer(np.linspace(-2, 2, 30), np.ones(30))
# Obtener la transpuesta de x
# Esto generará una especie de rejilla en 2D (x,y)
y = x.copy().T
# y se halla la función z(x,y)
z = np.cos(x ** 2 + y ** 2) + np.sin(x ** 2 + y ** 2)

fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot_surface(x, y, z,cmap='viridis', edgecolor='none')
ax.set_title('Gráfica de superficie')
plt.show()








