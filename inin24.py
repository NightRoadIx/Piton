'''
    PYAUTOGUI
    
    Se trata de una librería para el control de ciertas actividades
    de la GUI de la PC,generando scripts que controlan el ratón y el teclado,
    mostrar mensajes e interactuar con las ventanas
    Instalación:
        pip install pyautogui
'''   
#%%
import pyautogui

# Posición actual del ratón
print(pyautogui.position())
# Resolución de la pantalla
print(pyautogui.size())
# Tiempo muerto de 2.5 segundos
pyautogui.PAUSE = 2.5

#%%

# Funciones del ratón

# Mover el ratón a las coordenadas (x,y) tardando un total de n segundos
pyautogui.moveTo(5, 5, duration=1) # move mouse to XY coordinates over num_second seconds
# Mover el mouse un total de (x,y) relativos a su posición actual
pyautogui.moveRel(20, 30, duration=5)

# Si se desea dar clic moviendo el mouse a (x,y) posición, con un número de clics, con un intervalo de n segundos y que botón
pyautogui.click(x=5, y=5, clicks=1, interval=1, button='left')

# Se puede hacer "scroll" de la misma forma que al utilizar el botón medio
# con una cierta cantidad, moviendo el ratón a (x,y) coordenadas
pyautogui.scroll(100, 50, 50)

# Los eventos de clic up/down en el ratón pueden ser llamados de manera separada
pyautogui.mouseDown(x = 100, y = 100, button = 'left')
pyautogui.mouseUp(x = 100, y = 100, button = 'left')

#%%

# Funciones del teclado
# Para que se escriba algo en el teclado con un cierto intervalo en segundos
pyautogui.typewrite("Estoy escribiendo algo", interval=0.2)

# También se pueden pasar secuencias de teclas
pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=0.5)
# La lista completa de nombres de teclas se puede obtener tecleando pyautogui.KEYBOARD_KEYS

# Para combinaciones de teclas se puede utilizar
# Ctrl + C
pyautogui.hotkey('ctrl', 'c')

#%%

# Regresa el valor en texto del botón presionado
bot1 = pyautogui.alert('Este mensaje muestra texto con un botón OK', title='Ventanita1')
print(bot1)
# Regresa el valor en texto del botón presionado
bot2 = pyautogui.confirm('Este muestra texto con los botones OK y Cancel', title='Ventanita2')
print(bot2)
# regresa el texto ingresado
texto = pyautogui.prompt('Este permite ingresar texto y lo retorna al presionar OK', title='Ventanita3')
print(texto)
# regresa el texto ingresado
passw = pyautogui.password('Esta permite ingresar un password y esconderlo', title='Ventanita4', mask='*')
print(passw)



