# O problema não é variável não declarada, e sim que a função não retorna valor, apenas imprime; como não tem return, o Python considera que ela retorna None, então não é possível somar com 10.

def calcular_dobro(n):
    return n * 2

resultado = calcular_dobro(5) + 10
print(resultado)