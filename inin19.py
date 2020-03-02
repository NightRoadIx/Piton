'''
    GENERACIÓN DE ANIMACIONES
    Animaciones utilizando Matplotlib
'''
import numpy as np
from matplotlib import pyplot as plt
# Se requiere utilizar esta librería
from matplotlib.animation import FuncAnimation
# Aquí se pone como default el estilo de gráficaa utilizar en el script
plt.style.use('seaborn-pastel')

# Generar la figura
fig = plt.figure()
# Establecer los límites de la gráfica
ax = plt.axes(xlim=(0, 4), ylim=(-2, 2))
line, = ax.plot([], [], lw=3)

# Generar dos funciones
# Una para el inicio de los datos de las líneas a generar
# y así obtener un cuadro en blanco
def init():
    line.set_data([], [])
    return line,
# Otra para realizar la animación de cada cuadro
def animate(i):
    # Generar x en el intervalo [0,1000] con pasos de 4
    x = np.linspace(0, 4, 1000)
    # La función seno
    y = np.sin(2 * np.pi * (x - 0.01 * i))
    # Colocar los valores de los puntos (x,y)
    line.set_data(x, y)
    return line,

# Mandar a llamar la función FuncAnimation
# Revisar la siguiente página para observar las propieades:
# https://matplotlib.org/api/_as_gen/matplotlib.animation.FuncAnimation.html#matplotlib.animation.FuncAnimation
anim = FuncAnimation(fig, animate, init_func=init, frames=100, interval=1, blit=True)

# Guardar la animación en un archivo gif animado
anim.save('sine_wave.gif', writer='imagemagick')


#%%
# Generar una animación de una espiral
import matplotlib.animation as animation 
plt.style.use('dark_background')

fig = plt.figure() 
ax = plt.axes(xlim=(-50, 50), ylim=(-50, 50)) 
line, = ax.plot([], [], lw=2) 

# Función para iniciar la gráfica
def init(): 
	# Crear un cuadro vacío
	line.set_data([], []) 
	return line, 

# Lista para almacenar los puntos (x,y)
xdata, ydata = [], [] 

# Función para la animación
def animate(i): 
	# parámetro t
	t = 0.1*i 
	
	# los valores (x, y) a ser graficadas
	x = t*np.sin(t) 
	y = t*np.cos(t) 
	
	# adicionar puntos nuvos a la lista de posiciones
	xdata.append(x) 
	ydata.append(y) 
	line.set_data(xdata, ydata) 
	return line, 
	
# Crear un título para la gráfica
plt.title('Una espiral!!!!') 
# Esconder los ejes
plt.axis('off') 

# Mandar a llamar la función de animación
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=500, interval=20, blit=True) 

# Salvar la animación como un gif animado
anim.save('coil.gif',writer='imagemagick')


#%%
# Este ejemplo muestra la generación de una gráfica animada
# Debe ejecutarse desde consola
fig = plt.figure()
# Crear un subplot
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    data = open('stock.txt','r').read()
    lines = data.split('\n')
    xs = []
    ys = []
   
    for line in lines:
        # El delimitador de los datos es una coma
        x, y = line.split(',')
        xs.append(float(x))
        ys.append(float(y))
   
    
    ax1.clear()
    ax1.plot(xs, ys)

    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.title('Gráfica en vivo con Matplotlib')	
	
    
ani = animation.FuncAnimation(fig, animate, interval=1000) 
plt.show()
