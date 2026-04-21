playlist = []

while True:
    print("\n1 - ver playlist")
    print("2 - adicionar música")
    print("3 - remover música")
    print("4 - sair")

    opcao = input("escolha uma opção: ")

    if opcao == "1":
        if len(playlist) == 0:
            print("a playlist está vazia")
        else:
            print("músicas na playlist:")
            for musica in playlist:
                print("-", musica)

    elif opcao == "2":
        musica = input("qual música você quer adicionar? ")
        playlist.append(musica)
        print("música adicionada com sucesso")

    elif opcao == "3":
        musica = input("qual música você quer remover? ")
        if musica in playlist:
            playlist.remove(musica)
            print("música removida com sucesso")
        else:
            print("essa música não está na playlist")

    elif opcao == "4":
        print("saindo...")
        break

    else:
        print("opção inválida")