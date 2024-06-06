import tkinter as tk
from tkinter import PhotoImage
from PIL import ImageTk, Image
import serial
# pip install pyserial

# Establecer la conexión serial con el Arduino
arduino = serial.Serial('COM3', 9600, timeout=1)

# Crear la ventana principal de la aplicación
ventana = tk.Tk()
ventana.geometry("300x200")  # Definir el tamaño de la ventana
ventana.resizable(0, 0)  # No permitir cambiar el tamaño de la ventana
img = PhotoImage(file='led_encendido.png')
ventana.iconphoto(False, img)  # Establecer el ícono de la ventana
ventana.title("PYTHON + ARDUINO")  # Título de la ventana

# Función para mostrar la imagen del LED encendido
def imagen_led_encendido():
    # Cargar y redimensionar la imagen del LED encendido
    imagen_led = Image.open("led_encendido.png")
    nueva_imagen = imagen_led.resize((120, 120))
    render = ImageTk.PhotoImage(nueva_imagen)

    # Crear y colocar la etiqueta con la imagen en la ventana
    label_imagen = tk.Label(ventana, image=render)
    label_imagen.image = render  # Guardar referencia de la imagen para evitar que se borre
    label_imagen.place(x=40, y=40)  # Posicionar la imagen en la ventana

# Función para mostrar la imagen del LED apagado
def imagen_led_apagado():
    # Cargar y redimensionar la imagen del LED apagado
    imagen_led = Image.open("led_apagado.png")
    nueva_imagen = imagen_led.resize((120, 120))
    render = ImageTk.PhotoImage(nueva_imagen)

    # Crear y colocar la etiqueta con la imagen en la ventana
    label_imagen = tk.Label(ventana, image=render)
    label_imagen.image = render  # Guardar referencia de la imagen para evitar que se borre
    label_imagen.place(x=40, y=40)  # Posicionar la imagen en la ventana

# Función para enviar la señal de encendido al Arduino
def encender():
    print("ME PRENDE (Y MUCHO)")  # Imprimir en consola para ver el evento
    arduino.write(b'e')  # Enviar la señal de encendido al Arduino

# Función para enviar la señal de apagado al Arduino
def apagar():
    print("NO ME PRENDE (BUENO UN POQUITO)")  # Imprimir en consola para ver el evento
    arduino.write(b'a')  # Enviar la señal de apagado al Arduino

# Crear y colocar el texto en la ventana
texto = tk.Label(ventana, text="DIODO LED", font=("Arial", 12))
texto.place(x=60, y=15)  # Posicionar el texto en la ventana

# Crear y colocar el botón para encender el LED
boton_encender = tk.Button(text="Encender", command=lambda: [imagen_led_encendido(), encender()], height=2, width=10)
boton_encender.place(x=200, y=40)  # Posicionar el botón en la ventana

# Crear y colocar el botón para apagar el LED
boton_apagar = tk.Button(text="Apagar", command=lambda: [imagen_led_apagado(), apagar()], height=2, width=10)
boton_apagar.place(x=200, y=100)  # Posicionar el botón en la ventana

# Iniciar el bucle principal de la ventana
ventana.mainloop()

# Cerrar la conexión serial con el Arduino al cerrar la ventana
arduino.close()