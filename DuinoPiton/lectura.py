import serial
import time

# Ajustar el puerto:
# Windows: "COM3", "COM4", ...
# Linux: "/dev/ttyACM0" o "/dev/ttyUSB0"
# Mac: "/dev/tty.usbmodemXXXX" o similar
PUERTO = "COM6"
BAUDIOS = 9600

ser = serial.Serial(PUERTO, BAUDIOS, timeout=1)
time.sleep(2)  # Pausa corta para que Arduino reinicie

print("Leyendo datos, Ctrl+C para salir")
try:
  while True:
    linea = ser.readline().decode(errors="ignore").strip()
    if linea:
      print("Dato recibido:", linea)
except KeyboardInterrupt:
  print("Saliendo...")
finally:
  ser.close()
