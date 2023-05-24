# Librería para desarrollo de wep-apps
from flask import Flask, render_template
from flask import request, redirect, url_for

# Instanciar un objeto Flask
app = Flask(__name__)

# Decorador que indica cual es la página principal
# o raíz
@app.route('/')
def home():
    return "Lady, lady bug"

@app.route('/welcome') # https://www.saes.ipn.mx/welcome
def ganesha():
    return render_template('welcome.html')

# Página hechiza
@app.route('/p/<string:hector>/')
def mostrar_sela(hector=None):
    return render_template(
        'hechiza.html',
        titulo=hector
    )
    # return f'Mostrando: {hector}'

# Página de inicio
@app.route('/signup/', methods=['GET', 'POST'], )
def darAlta():
    if request.method == 'POST':
        nombre = request.form['name']
        email = request.form['email']
        password = request.form['password']

        next = request.args.get('next', None)
        if next:
            return redirect(next)
        return render_template(url_for('home'))
    return render_template('alta.html')

# Iniciamos el servidor
if __name__ == '__main__':
    # Iniciar la aplicación
    # en modo Debug / Producción
    app.run(debug=True)