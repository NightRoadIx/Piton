import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Generar una clase
# Una clase es una especie de contenedor o plantilla que
# abstrae objetos de la realidad definiendo cómo puede describirse (atributos)
# y que funcionalidades tienen (métodos)
class AnimationPlot:

    def animate(self, i, dataList, ser):
        # Transmirir el caracter g para recibir datos del sistema embebido
        ser.write(b'g')
        # Decodificar los datos recibidos como una cadena con formato
        # i es una variable incremental basada en cuadros = x argumento
        arduinoData_string = ser.readline().decode('ascii')
        # print(i)

        try:
            # Convertir a un número de punto flotante
            arduinoData_float = float(arduinoData_string)
            # Añadir a la lista
            dataList.append(arduinoData_float)

        except:
            pass    # No hacer nada si los datos recibidos son incorrectos
        # Fijar el tamaño de la lista para que la ventana de animación sea un número x de puntos
        dataList = dataList[-50:]

        # Limpiar el último cuadro de datos
        ax.clear()

        self.getPlotFormat()
        # Graficar el nuevo cuadro de datos
        ax.plot(dataList)

    def getPlotFormat(self):
        # Colocar el límite del eje Y
        ax.set_ylim([0, 1200])
        ax.set_title("Datos seriales")
        ax.set_ylabel("Valor [V]")

# Crear una variable lista para los datos
dataList = []

fig = plt.figure()
ax = fig.add_subplot(111)

# Se genera un objeto del tipo AnimationPlot
realTimePlot = AnimationPlot()

# Configurar el puerto serial
ser = serial.Serial("COM8", 9600)
# Un pequeño delay para esperar el inicio del puerto Serial
time.sleep(2)

# Función para Animar, pasando los valores de la figura donde animar, la función para generar los datos
# La cantidad de recuadros, se pasan los argumentos de la lista de datos y el puerto serial
# y el intervalo de tiempo
ani = animation.FuncAnimation(fig, realTimePlot.animate, frames=100, fargs=(dataList, ser), interval=100)

plt.show()
ser.close()