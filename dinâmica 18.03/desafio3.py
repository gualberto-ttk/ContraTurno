# O problema é que input() retorna texto (string), e não número. Não é possível somar string com inteiro.

preco = float(input("Digite o preço: "))
novo_preco = preco + 5
print("O valor final é:", novo_preco)