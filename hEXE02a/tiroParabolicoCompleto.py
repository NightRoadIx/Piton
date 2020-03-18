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

# Ingresar los datos
v0 = limite("velocidad inicial (m/s): ", 0, 1000000)
al0 = limite("ángulo inicial (°)    : ", 0, 180)
h0 = limite("altura inicial (m)     : ", -0.0001, 1000000)
g = limite("gravedad (m/s\u00B2)    : ", 0, 1000000)
dt = int(limite("cantidad de pasos de la simulación: ", 0, 1000))
# Ingresar el nombre del archivo a almacenar
archon = input("Ingresar el nombre del archivo a guardar: ")
# Generar el nombre con extensión
archon += '.txt'

# Cálculos iniciales
th0 = al0 * np.pi / 180
x = np.linspace(0, ((((v0**2)*np.sin(2*th0))/g)), dt)
y = x*np.tan(th0) - 0.5 * g * (x / (v0*np.cos(th0)))**2 + h0

# Abrir el archivo para escritura
f = open(archon, "w")
f.write("-- TIRO PARABÓLICO --\n")
f.write("{:10}\t{:10}\t{:10}\t{:10}\n".format('Paso', 'x', 'y', 'dt'))

for k in range(dt):
    testo = "{:10}\t{:10}\t{:10}\t{:10}\n".format(k, round(x[k], 10), round(y[k], 10), round(x[k]/(v0*np.cos(th0)), 10))
    f.writelines(testo)
f.close()

plt.plot( x, y, "-",linewidth=4,color=(1,0,0))
plt.title("Tiro Parabólico")
plt.xlabel("Distancia [m]")
plt.ylabel("Altura [m]")
plt.grid()
plt.show()
print("Máxima altura alcanzada {:} m".format(round(max(y), 4)))
print("Máxima distancia alcanzada {:} m".format(round(max(x), 4)))
