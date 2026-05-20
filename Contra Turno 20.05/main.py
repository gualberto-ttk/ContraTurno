from flask import Flask, render_template, request
import webbrowser
from threading import Timer

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('formulario.html')

@app.route('/resultado')
def resultado():
    return render_template('resultado.html',
        nome=request.args.get('nome'),
        curso=request.args.get('curso'),
        cidade=request.args.get('cidade'),
        email=request.args.get('email')
    )

Timer(1, lambda: webbrowser.open('http://127.0.0.1:5000')).start()
app.run(debug=True)