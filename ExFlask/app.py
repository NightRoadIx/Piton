# Importar la librería del framework Flask
from flask import Flask, render_template, request
from forms import UserForm

# Se instancia el objeto Flask
app = Flask(__name__)

# Iniciar un diccionario vacío para guardar los datos
data = {}
# Contador de usuarios
user_id_counter = 1

'''
    En aplicaciones web, hay métodos para el envío de datos
    entre un cliente (navegador web) y un servidor.
    Son parte del protocolo HTTP que define como se formatean
    y transmiten los mensajes en la web.
    Entre los más comúnes se encuentran GET y POST.
    GET
        Solicita datos de un servidor, enviando parámetros
        por la URL. Es el método más común para solicitar
        una página web.
    POST
        Envía datos al servidor para que lo procese y esto
        puede resultar en un cambio en el mismo servidor, 
        como agregar datos a una BD.
        Es utilizado comúnmente cuando se envían formularios
        en la página web. 
'''

# Para la dirección raíz (GET)
@app.route("/")
def index():
    # Regresa la página a la que se ingresa
    # cuando entra a raíz del sitio web
    print("Entro a root")
    # esto mediante la función render_template("pagina.html")
    return render_template("form.html")

# Para el caso de entrar al apartado users (GET)
@app.route("/users")
def users():
    print("Ingresó a users")
    return render_template("users.html", users=data.values())

# Para el caso de entrar al apartado submit (POST)
@app.route("/submit", methods=["POST"])
def submit():
    global data  # Declarar como variable global
    try:
        # Obtener el formulario como objeto
        form = UserForm(request.form)

        # si el formulario es válido
        if form.validate():
            global user_id_counter

            # Obtener los datos del formulario
            username = request.form["username"] # Usuario
            email = request.form["email"]       # Correo

            # Añadir los datos al diccionario
            data[user_id_counter] = {'id': user_id_counter, 'username': username, 'email': email}
            user_id_counter += 1

            return "Usuario añadido exitósamente"
        else:
            # Regresar el mensaje de error
            return 'Datos inválidos, intente de nuevo'
    except Exception as e:
        return f"Ocurrió un error mortal del tipo: {str(e)}"

if __name__ == "__main__":
    # Ejecutar en modo prueba (DEBUG)
    app.run(debug=True)