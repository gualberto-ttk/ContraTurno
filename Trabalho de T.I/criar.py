from playlists import playlists

def criar_playlist():
    nome = input("nome da playlist: ")

    if nome == "":
        print("nome invalido")
    else:
        if nome in playlists:
            print("ja existe")
        else:
            playlists[nome] = []
            print("playlist criada")