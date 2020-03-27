'''
    ENVIO DE CORREOS MEDIANTE PYTHON
'''
# Importar la libreria para mandar paquetes mediante SMTP
# Simple Mail Transfer Protocol
# el cual es el protocolo para envío de mensajes por medio del correo electrónico
# junto con la librería SSL (Secure Sockets Layer) la cual está diseñada para
# crear conexiones seguras entr eun cliente y el servidor
import smtplib, ssl

# Crear el contexto
context = ssl.create_default_context()

# Usar la instrucción with, la cual permite ejecutar la instrucción que se
# coloca dentro de ella, algo parecido a un try-except
# Se hace una petición SMTP al servidor de Gmail sobre el puerto 465
# https://www.redeszone.net/tutoriales/configuracion-puertos/puertos-tcp-udp/
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    # Una vez hecho esto colocar aquí el nombre del correo de gmail junto con la contraseña
    server.login('correo@8gmail.com', 'contresenna')
    # Ahora enviar cosas del correo a otro, se escribe el mensaje
    server.sendmail('correo@gmail.com', 'correoDestino@loquesea.com', 'Mensaje')
    # Cerrar el servidor
    server.close()
