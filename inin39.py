# Importar los módulos
import tkinter 
import random 
  
# Lista de los posible colores (se usa la lista en inglés para el color)
colors = ['Red','Blue','Green','Pink','Black', 
           'Yellow','Orange','White','Purple','Brown']
# y en español para el juego
colores = ['Rojo','Azul','Verde','Rosa','Negro',
           'Amarillo','Naranja','Blanco','Morado','Café']
# Empaquetar los objetos a partir de las listas
zipObj = zip(colors, colores)
# Crear el diccionario
colours = dict(zipObj)
# Mandar a crerar las llaves o indices del diccionario
llaves = list(colours.keys())

# Iniciar la puntuación
score = 0
  
# El tiempo que queda del juego, iniciando en 30 segundos
timeleft = 30
  
# ----------------------------------------------------------------------------
# La función para el inicio del juego
def startGame(event):
    
    # Cuando el tiempo va iniciando
    if timeleft == 30: 
          
        # Iniciar el contador descendente (temporizador)
        countdown() 
          
    # Correr la función para elegir el siguiente color
    nextColour() 

# ----------------------------------------------------------------------------  
# Función para escoger y desplegar el color
def nextColour(): 
  
    # Estas dos variables se declararán como globales para usarse en todo el 
    # programa y fuciones
    global score 
    global timeleft 
  
    # Cuando se está jugando (el tiempo aún no ha terminado)
    if timeleft > 0: 
  
        # Colocar el foco de selección en la caja de texto
        e.focus_set() 
  
        # Si el color ingresado es igual al color del texto
        # todo en minúsculas
        if e.get().lower() == colours[llaves[1]].lower(): 
            # Se incrementa el puntaje
            score += 1

        # limpiar la caja de entrada
        e.delete(0, tkinter.END) 

        # Cambiar el orden de la lista (de las llaves o claves del diccionario)
        random.shuffle(llaves) 
          
        # Cambiar el tanto el texto como el color de las letras
        # el color se cambia a partir de las claves (en inglés)
        # y el texto en español
        label.config(fg = str(llaves[1]), text = str(colours[llaves[0]])) 
          
        # Actualizar el puntaje
        scoreLabel.config(text = "Puntaje: " + str(score)) 
  
# ----------------------------------------------------------------------------
# Función del timer conteo
def countdown(): 
  
    global timeleft
  
    # Cuando se está jugando (el tiempo aún no ha terminado)
    if timeleft > 0: 
  
        # Disminuir el tiempo que queda
        timeleft -= 1
          
        # Actualizar la etiqueta del tiempo que queda
        timeLabel.config(text = "Tiempo restante: " + str(timeleft))
        if timeleft < 5:
            timeLabel.config(fg = "red")
                                 
        # Ejecutar la función de nuevo tras un segundo
        timeLabel.after(1000, countdown)
    elif timeleft == 0:
        e.configure(state='disabled')
  
# ---------------------------------------------------------------------------- 
# MAIN
  
# Crear la ventana GUI
root = tkinter.Tk() 
  
# Colocar el título
root.title("JUEGO DE COLOR")
  
# Colocar el tamaño de la ventana
root.geometry("375x200") 

# Cambiar el ícono de la ventana
root.iconbitmap('parasito.ico')
  
# Colocar una etiqueta de instrucciones
instructions = tkinter.Label(root, text = "Escribir el color en palabras y no la palabra", font = ('Helvetica', 12)) 
instructions.pack()  
  
# Añadir la etiqueta del puntaje
scoreLabel = tkinter.Label(root, text = "Presionar Enter para iniciar", font = ('Helvetica', 12)) 
scoreLabel.pack() 
  
# Añadir la etiqueta del tiempo que queda
timeLabel = tkinter.Label(root, text = "Tiempo restante: " + str(timeleft), font = ('Helvetica', 12)) 
                
timeLabel.pack() 
  
# Añadir una etiqueta para mostrar los colores
label = tkinter.Label(root, font = ('Helvetica', 60)) 
label.pack() 
  
# Añadir una caja de texto para escribir los colores
e = tkinter.Entry(root) 
  
# Ejecutar ña función de inicio del juego
# Cuando la tecla Enter sea presionada
root.bind('<Return>', startGame) 
e.pack() 
  
# Colocar el foco en la caja de entrada
e.focus_set() 
  
# Iniciar la GUI

root.mainloop() 