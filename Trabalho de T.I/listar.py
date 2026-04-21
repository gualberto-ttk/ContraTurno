from playlists import playlists

def listar():
    if len(playlists) == 0:
        print("nao tem nada")

    else:
        for p in playlists:
            print("\nplaylist:", p)

            if len(playlists[p]) == 0:
                print("sem musicas")
            else:
                for m in playlists[p]:
                    print("-", m)