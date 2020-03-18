#%%
import numpy as np
import matplotlib.pyplot as plt
import random as rd

# Función para delimitar los datos a ingresar
def limite(cad, a):
    val = 0
    while True:
        val = float(input("Ingresar " + cad))
        if (val > a):
            break
    return val

# Ingresar los valores
L = limite('la longitud del paso: ', 0)
N = int(limite('número de pasos     : ', 0))

# U a vez hecho esto se generan los vectores
x = np.zeros(N+1)
y = np.zeros(N+1)
d = np.zeros(N+1)

for k in range(1, N+1):
    # Obtener el ángulo en forma aleatoria (intervalo [0, 2pi])
    alfa = rd.uniform(0, 2*np.pi)
    
    # Obtener las coordenadas de los avances
    x_paso = L * np.cos(alfa)
    y_paso = L * np.sin(alfa)
    
    # Incrementar la posición del sujeto
    x[k] = x[k-1] + x_paso
    y[k] = y[k-1] + y_paso
    # Distancia hasta ese punto
    d[k] = np.sqrt( x[k]**2 + y[k]**2 )

plt.plot(x, y, ".", color=(1,0,0))
plt.plot(x, y, "-", color=(0,0,1))
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.grid()
plt.show()