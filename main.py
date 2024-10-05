# Import
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# Página de contenidos en ejecución
@app.route('/')
def index():
    return render_template('index.html')


# Habilidades dinámicas
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    return render_template('index.html', button_python=button_python)

@app.route('/info')
def info():
    return render_template('info.html')

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html')
    

if __name__ == "__main__":
    app.run(debug=True)
