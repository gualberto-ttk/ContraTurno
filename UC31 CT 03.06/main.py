from flask import Flask, render_template, request
import webbrowser
from threading import Timer

app = Flask(__name__)

def abrir():
    webbrowser.open("http://127.0.0.1:5000")

@app.route("/", methods=["GET", "POST"])
def cadastro():

    erros = []
    aluno = {}

    if request.method == "POST":

        nome = request.form.get("nome").strip()
        email = request.form.get("email").strip()
        telefone = request.form.get("telefone").strip()
        cpf = request.form.get("cpf").strip()
        cidade = request.form.get("cidade").strip()
        estado = request.form.get("estado").strip()
        curso = request.form.get("curso").strip()
        idade = request.form.get("idade").strip()
        senha = request.form.get("senha").strip()

        nome = nome.title()
        email = email.lower()
        cidade = cidade.title()
        estado = estado.upper()

        telefone = telefone.replace("(", "")
        telefone = telefone.replace(")", "")
        telefone = telefone.replace("-", "")
        telefone = telefone.replace(" ", "")

        cpf = cpf.replace(".", "")
        cpf = cpf.replace("-", "")

        if nome == "" or email == "" or telefone == "" or cpf == "" or cidade == "" or estado == "" or curso == "" or idade == "" or senha == "":
            erros.append("Preencha todos os campos obrigatórios.")

        if len(nome) < 8:
            erros.append("Nome inválido.")

        if "@" not in email or ".com" not in email:
            erros.append("E-mail inválido.")

        if len(telefone) != 11:
            erros.append("Telefone inválido.")

        if len(cpf) != 11:
            erros.append("CPF inválido.")

        if len(cidade) < 3:
            erros.append("Cidade inválida.")

        if len(estado) != 2:
            erros.append("Estado inválido.")

        if idade.isdigit():
            if int(idade) < 16:
                erros.append("Idade inválida.")
        else:
            erros.append("Idade inválida.")

        tem_numero = False

        for letra in senha:
            if letra.isdigit():
                tem_numero = True

        if len(senha) < 8:
            erros.append("Senha muito fraca.")

        if tem_numero == False:
            erros.append("Senha muito fraca.")

        if len(erros) == 0:

            aluno["nome"] = nome
            aluno["email"] = email
            aluno["telefone"] = telefone
            aluno["cpf"] = cpf
            aluno["cidade"] = cidade
            aluno["estado"] = estado
            aluno["curso"] = curso
            aluno["idade"] = idade

    return render_template("cadastro.html", erros=erros, aluno=aluno)

if __name__ == "__main__":
    Timer(1, abrir).start()
    app.run(debug=True)