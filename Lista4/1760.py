#1760 - Pesquisa - Idade e Peso - Python

contador = 4

pessoasPesadas = 0

idade = 0

while contador > 0:
    idadePessoa = int(input())
    peso = float(input())

    if peso > 90:
        pessoasPesadas = pessoasPesadas + 1
        idade = idade + idadePessoa
        contador = contador - 1 

    else:
        idade = idade + idadePessoa
        contador = contador - 1

media = idade / 4

print("Qtd pessoas > 90 Kg: %i"%(pessoasPesadas))
print("Idade média: %.2f"%(media))