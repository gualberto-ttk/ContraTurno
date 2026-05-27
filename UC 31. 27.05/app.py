from flask import Flask, render_template
import webbrowser
from threading import Timer

app = Flask(__name__)

def abrir_navegador():
    webbrowser.open("http://127.0.0.1:5000/")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/cursos")
def cursos():
    return render_template("cursos.html")

@app.route("/professores")
def professores():
    return render_template("professores.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    Timer(1, abrir_navegador).start()
    app.run(debug=True)