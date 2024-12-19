# Importar los módulos necesarios
from tkinter import *  # Librería estándar para crear interfaces gráficas en Python
import customtkinter  # Librería para generar componentes personalizados con apariencia moderna
from PIL import Image  # Librería para manejar imágenes (parte de Pillow)

# Configuración de apariencia para el framework CustomTkinter
customtkinter.set_appearance_mode("dark")  # Establece el modo oscuro para la interfaz

# Configuración de colores predeterminados para los componentes
# "green" establece una paleta de colores verde para los botones y elementos
customtkinter.set_default_color_theme("green")

# Crear la ventana principal (root) usando el constructor de CustomTkinter
root = customtkinter.CTk()

# Cargar la imagen que se usará en el botón
# Se configura la misma imagen para los modos claro y oscuro
imagen = customtkinter.CTkImage(
    light_image=Image.open("led_encendido.png"),  # Imagen en modo claro
    dark_image=Image.open("led_encendido.png"),  # Imagen en modo oscuro
    size=(30, 30)  # Tamaño al que se redimensiona la imagen
)

# Configuración del tamaño de la ventana principal
root.geometry("300x400")  # La ventana tendrá un tamaño de 300 px de ancho y 400 px de alto

# Evitar que el usuario cambie el tamaño de la ventana
root.resizable(False, False)

# Crear un botón con varios atributos personalizados
boton = customtkinter.CTkButton(
    master=root,  # Asociar el botón a la ventana principal
    text="",  # Texto del botón (vacío en este caso)
    corner_radius=48,  # Radio de las esquinas para darle un estilo redondeado
    fg_color="#FF0000",  # Color de fondo del botón (en este caso, rojo)
    font=("Arial", 14, 'bold'),  # Fuente del texto (aunque no se usa porque el texto está vacío)
    image=imagen,  # Imagen que se mostrará en el botón
    width=30,  # Ancho del botón
    height=30  # Alto del botón
)

# Posicionar el botón en la ventana principal
boton.place(
    relx=0.5,  # Posición relativa en el eje X (0.5 significa al centro horizontalmente)
    rely=0.5,  # Posición relativa en el eje Y (0.5 significa al centro verticalmente)
    anchor=CENTER  # Anclar el botón desde su centro
)

# Iniciar el bucle principal de la ventana
# Esto mantiene la ventana abierta y en espera de interacciones del usuario
root.mainloop()
