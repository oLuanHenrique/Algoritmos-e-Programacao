#1737 - Soma Números - Python

qtd = int(input())
soma = 0
contador= 0 

if qtd<=0:
    print("Informe uma quantidade > 0!")
    
else:
    while contador < qtd:
        num = float(input())
        soma = soma + num
        contador = contador + 1
    print("Soma dos números informados:%.2f" %(soma))