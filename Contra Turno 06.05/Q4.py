from flask import Flask

app = Flask(__name__)

@app.route('/operacao/<tipo>/<int:op1>/<int:op2>')
def operacao(tipo, op1, op2):

    if tipo == "sum":
        return str(op1 + op2)

    elif tipo == "sub":
        return str(op1 - op2)

    elif tipo == "mult":
        return str(op1 * op2)

    elif tipo == "div":
        return str(op1 / op2)

    return "erro"