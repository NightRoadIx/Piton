import pandas as pd
import matplotlib.pyplot as plt

# Marcar que se utilizará un estilo con fondo oscuro
plt.style.use("dark_background")

# Aquí se genera el color de las letras
for param in ['text.color', 'axes.labelcolor', 'xtick.color', 'ytick.color']:
    plt.rcParams[param] = '0.9'  # gris claro
# En este se genera el color del fondo de la gráfica
for param in ['figure.facecolor', 'axes.facecolor', 'savefig.facecolor']:
    plt.rcParams[param] = '#1E2247'  # gris azulada oscuro
    
# Se crea una lista con colores
colors = [
    '#08F7FE',  # cian
    '#FE53BB',  # rosado
    '#F5D300',  # amarillo
    '#00ff41',  # verde matrix
]

# Se usa el pandas para crear un DataFrame, que contiene ciertos datos que se
# van a graficar
df = pd.DataFrame({'A': [1, 3, 9, 5, 2, 1, 1],
                   'B': [4, 5, 5, 7, 9, 8, 6],
                   'C': [2, 1, 8, 6, 4, 2, 4],
                   'D': [6, 4, 2, 3, 6, 7, 5]})

# Crear los ejes para la gráfica
fig, ax = plt.subplots()
# Se usará como marcador 'o', los colores previamente colocados
df.plot(marker='o', color=colors, ax=ax)

# Graficar los datos con un alpha (nivel de transparencia) bajo
# y un ancho de línea ligeramente más ancho
n_shades = 10
diff_linewidth = 1.05
alpha_value = 0.3 / n_shades
# Ahora si colocar los valores de los colores de las líneas
for n in range(1, n_shades+1):
    df.plot(marker='o',
            linewidth=2+(diff_linewidth*n),
            alpha=alpha_value,
            legend=False,
            ax=ax,
            color=colors)
# Colorear las áreas debajo de las líneas
for column, color in zip(df, colors):
    ax.fill_between(x=df.index,
                    y1=df[column].values,
                    y2=[0] * len(df),
                    color=color,
                    alpha=0.1)
ax.grid(color='#2A3459')
# Para no cortar los marcadores
ax.set_xlim([ax.get_xlim()[0] - 0.2, ax.get_xlim()[1] + 0.2])  # to not have the markers cut 
ax.set_ylim(0)
plt.show()