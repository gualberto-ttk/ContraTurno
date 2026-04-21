from playlists import playlists

def remover():
    if len(playlists) == 0:
        print("sem playlist")

    else:
        print(playlists.keys())

        p = input("qual playlist: ")

        if p not in playlists:
            print("nao existe")

        else:
            if len(playlists[p]) == 0:
                print("vazia")

            else:
                print(playlists[p])

                m = input("qual remover: ")

                if m in playlists[p]:
                    playlists[p].remove(m)
                    print("removida")
                else:
                    print("nao encontrada")