catalogo = {}
emprestimos = []

def adicionarLivro(codigo, titulo, autor, quantidade):
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

def emprestarLivro(codigo, usuario):
    if codigo in catalogo and catalogo[codigo]["quantidade"] > 0:
        emprestimos.append({
            "codigo": codigo,
            "titulo": catalogo[codigo]["titulo"],
            "usuario": usuario,
            "ativo": True
        })
        catalogo[codigo]["quantidade"] -= 1

def listarEmprestimosAtivos():
    for e in emprestimos:
        if e["ativo"]:
            print(e["titulo"], "-", e["usuario"])