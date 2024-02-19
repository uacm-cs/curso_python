from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Datos de usuarios (simulados para el ejemplo)
USUARIOS = {
    'usuario1': 'u1',
    'usuario2': 'u2'
}



@app.route('/')
def root():
        return render_template('login.html')


@app.route('/inicio')
def inicio():
        return "Inicio del sistema"



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['usuario']
        password = request.form['contrasena']
        if username in USUARIOS and USUARIOS[username] == password:
            # Iniciar sesión exitosa, redirigir a otra página
            return redirect(url_for('inicio'))
        else:
            # Credenciales incorrectas, mostrar mensaje de error
            return 'Credenciales incorrectas. <a href="/login">Intenta de nuevo</a>'
    else:
        #return render_template('login.html')
        return render_template('login2.html')
    


if __name__ == '__main__':
    app.run(debug=True)
