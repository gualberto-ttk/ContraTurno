from flask import Flask

app = Flask(__name__)

@app .route('/arearestrita/<int:id>')
def area(id):

    if id == 1:
        return "🔒"

    elif id == 2:
        return "🔓"

    return "id invalido"