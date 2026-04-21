from criar import criar_playlist
from adicionar import adicionar_musica
from listar import listar
from remover import remover
from sair import sair

while True:
    print("\nMENU")
    print("1 criar playlist")
    print("2 adicionar musica")
    print("3 listar playlists")
    print("4 remover musica")
    print("5 sair")

    op = input("escolha: ")

    if op == "1":
        criar_playlist()

    elif op == "2":
        adicionar_musica()

    elif op == "3":
        listar()

    elif op == "4":
        remover()

    elif op == "5":
        sair()
        break

    else:
        print("opcao invalida")