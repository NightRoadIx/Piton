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

def menu():
    print("Paseo aleatorio")
    print("1.- Paseo aleatorio en todo el plano cartesiano, paso fijo")
    print("2.- Paseo aleatorio y positivo, paso fijo")
    print("3.- Paseo aleatorio en un solo cuadrante, paso fijo")
    print("4.- Paseo aleatorio en todo el plano, paso aleatorio")
    return int(input('Opción ->'))

# MAIN
# Llamar al menú
opc = menu()
# Ingresar los valores
L = limite('Longitud máxima del paso: ', 0)
N = int(limite('número de pasos     : ', 0))
if(opc == 3):
    cuad = int(limite('Cuadrante     : ', 0))

# U a vez hecho esto se generan los vectores
x = np.zeros(N+1)
y = np.zeros(N+1)
d = np.zeros(N+1)

for k in range(1, N+1):
    
    while True:
        # Obtener el ángulo en forma aleatoria (intervalo [0, 2pi])
        alfa = rd.uniform(0, 2*np.pi)
        if(opc == 4):
            # Obtener la longitud del paso de forma aleatoria (intervalo (0, L])
            La = rd.uniform(0, L)
        else:
            La = L
        
        # Obtener las coordenadas de los avances
        x_paso = La * np.cos(alfa)
        y_paso = La * np.sin(alfa)
        
        # Incrementar la posición del sujeto
        x[k] = x[k-1] + x_paso
        y[k] = y[k-1] + y_paso
        
        if( (opc == 1)or(opc == 4) ):
            break
        else:
            if( opc == 2 ):
                if( y[k] > 0 ):
                    break
            elif( opc == 3 ):
                if( cuad == 1 ):
                    if ( (x[k] > 0)and(y[k] > 0) ):
                        break
                if( cuad == 2 ):
                    if ((x[k] < 0)and(y[k] > 0)):
                        break
                if( cuad == 3 ):
                    if ((x[k] < 0)and(y[k] < 0)):
                        break
                if( cuad == 4 ):
                    if ((x[k] > 0)and(y[k] < 0)):
                        break 


plt.plot(x, y, ".", color=(1,0,0))
plt.plot(x, y, "-", color=(0,0,1))
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.grid()
plt.show()