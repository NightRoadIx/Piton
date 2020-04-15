#%%
import numpy as np
import matplotlib.pyplot as plt

# Función para delimitar los datos a ingresar
def limite(cad, a, b):
    val = 0
    while True:
        val = float(input("Ingresar " + cad))
        if (val > a) and (val < b):
            break
    return val

# Función para simular el tiro parabólico
def simula(caso, v0, al0, h0, v_x_0, v_y_0, g, re, C_drag, rho, Ar, m, dt, arc):
    # Cálculos iniciales
    # Contador i (pasos de la simulación)
    i = 0
    # Iniciar los valores de la posición
    x = [0]
    y = [h0]
    # Iniciar los valores de la velocidad
    v_x = v_x_0
    v_y = v_y_0
    # Iniciar valores de la acelaración
    a_x = 0
    a_y = 0
    
    # Archivo para guardar datos
    f = open( arc + "_" + str(caso) + ".txt" ,"w")
    
    ##############################################################################
    # Simulación
    f.write("---Caso {}---\n". format(caso))
    f.write("Velocidad inicial        : {} m/s\n".format(v0))
    f.write("Ángulo inicial           : {} °\n".format(al0))
    f.write("Altura inicial           : {} m\n".format(h0))
    f.write("Masa proyectil           : {} kg\n".format(m))
    f.write("Área del proyectil       : {} m^s\n".format(Ar))
    f.write("Coeficiente aerodinámico : {} \n".format(C_drag))
        
    print("{0} {1} {2} {3} {4} {5}".format('i'.rjust(6,' '), 'x'.rjust(12, ' '), 'y'.rjust(12, ' '), '\u0394t'.rjust(12, ' '), 'g [m/s\u00B2]'.rjust(12, ' '), '\u03C1 [kg/m\u00B3]'.rjust(12, ' ')))
    f.write( "{0} {1} {2} {3} {4} {5}\n".format('i'.rjust(6,' '), 'x'.rjust(12, ' '), 'y'.rjust(12, ' '), 'dt'.rjust(12, ' '), 'g [m/s^2]'.rjust(12, ' '), 'rho [kg/m^3]'.rjust(12, ' ')) )
    while True:
        # Caso 1, IDEAL
        if(caso == 1):
            # No hay cambio en la fricción por el aire
            rho = 0
            # Aceleración de la gravedad no cambia
            gc = g
        # Caso 2, FRICCIÓN
        if(caso == 2):
            rho = rho
        # Solo mantener aceleración de la gravedad
            gc = g
        if(caso == 3):
            # Calcular la densidad del aire que cambia en función de la altura
            # Se considera que la altura inicial está a nivel del mar
            rho = -0.0001031*y[i] + 1.216
            # Aceleración de la gravedad no cambia
            gc = g
        if(caso == 4):
            # Calcular la densidad del aire que cambia en función de la altura
            # Se considera que la altura inicial está a nivel del mar
            rho = -0.0001031*y[i] + 1.216
            # Calcular la gravedad con respecto a la altura
            # de la misma forma se calcula con respecto del nivel del mar
            gc = g*( ( re/(re+y[i]) )**2 )
        
        # Calcular el ángulo del vuelo
        angle = np.tan( v_y/v_x )
                
        # Calcular aceleraciones
        a_x = -C_drag*0.5*rho*Ar*(v_x**2 + v_y**2)/m*np.cos(angle)
        a_y = -gc - C_drag*0.5*rho*Ar*(v_x**2 + v_y**2)/m*np.sin(angle)
        
        print("{0:6d} {1:12.4f} {2:12.4f} {3:12.4f} {4:12.4f} {5:12.4f}".format(i, x[i], y[i], i*dt, gc, rho))
        f.write("{0:6d} {1:12.4f} {2:12.4f} {3:12.4f} {4:12.4f} {5:12.4f}\n".format(i, x[i], y[i], i*dt, gc, rho))
        
        # Calcular velocidades
        v_x = v_x + a_x * dt
        v_y = v_y + a_y * dt
                
        # Cuando el proyectil pase por debajo del suelo
        if( y[i] < 0 ):
            break
        
        # Calcular posiciones
        x.append( x[i] + v_x*dt + (1/2)*a_x*(dt**2) )
        y.append( y[i] + v_y*dt + (1/2)*a_y*(dt**2) )
        
        # Incrementar contador
        i += 1
    
    # Cerrar archivo
    f.close()
    # Valores a regresar
    # Observar queen Python se pueden regresar m+ultiples valores a partir de
    # una función
    return x, y

##############################################################################
# Ingresar los datos
'''
v0  = limite("velocidad inicial (m/s): ", 0, 1000000)
al0 = limite("ángulo inicial (°)    : ", 0, 180)
h0  = limite("altura inicial (m)     : ", -0.0001, 1000000)
m   = limite("masa del proyectil (kg) : ", 0, 10000)
Ar  = limite("Área del proyectil (m\u00B2) : ", 0, 10000) 
C_drag = limite("Coeficiente aerodinámico del proyectil () : ", 0, 10000)
g   = limite("gravedad (m/s\u00B2)    : ", 0, 1000)
re = limite("Radio del planeta: [m] :", 0, 10000000)
rho = limite("densidad del aire (kg m-\u00B3) : ", 0, 1000)
dt = limite("Intervalo de tiempo de simulación (s): ", 0, 1000)
# Ingresar el nombre del archivo a almacenar
archon = input("Ingresar el nombre del archivo a guardar: ")
# Generar el nombre con extensión
archon += '.txt'
'''
v0 = 20.2498
al0 = 87.1376
h0 = 0
m = 1.82
Ar = 1.02e-2
C_drag = 0.25
g= 9.80665
rho = 1.2254
dt = 0.1
# Radio de la tierra en metros
re = 6371000
archon = "prueba"

#%%
##############################################################################
# Cálculos iniciales
# Ángulo en radianes inicial
th0 = al0 * np.pi / 180
# Velocidades iniciales
v_x_0 = v0 * np.cos(th0)
v_y_0 = v0 * np.sin(th0)

# Simulaciones
x, y = simula(1, v0, al0, h0, v_x_0, v_y_0, g, re, C_drag, rho, Ar, m, dt, archon)
x1, y1 = simula(2, v0, al0, h0, v_x_0, v_y_0, g, re, C_drag, rho, Ar, m, dt, archon)
x2, y2 = simula(3, v0, al0, h0, v_x_0, v_y_0, g, re, C_drag, rho, Ar, m, dt, archon)
x3, y3 = simula(4, v0, al0, h0, v_x_0, v_y_0, g, re, C_drag, rho, Ar, m, dt, archon)


##############################################################################
# GRAFICACIÓN
plt.plot(x, y, color=(1,0,0))
plt.plot(x1, y1, color=(0,0,1))
plt.plot(x2, y2, color=(0,0,0))
plt.plot(x3, y3, color=(0,1,0))
plt.xlabel('x [m]')
plt.ylabel('y [m]')
plt.legend(['Ideal','Fricción',r'Fricción, $ \Delta\rho_{aire} $ ',r'Fricción, $ \Delta\rho_{aire}  \Delta g $ '], loc='upper right')
plt.grid()
plt.savefig(archon + '_fig.png', transparent = True, dpi = 300)
plt.show()
