from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Datos de usuarios (simulados para el ejemplo)
USUARIOS = {
    'usuario1': 'u1',
    'usuario2': 'u2'
}



@app.route('/')
def inicio():
    return '¡Hola, mundo! Esta es mi primera aplicación Flask.'

if __name__ == '__main__':
    app.run(debug=True)
