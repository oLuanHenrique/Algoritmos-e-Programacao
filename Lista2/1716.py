#1716 - Plano de Trabalho - Python

p = input()
s = float(input())

if p == "A":
    aumento = s * 0.1
elif p =="B":
    aumento = s * 0.15
else:
    aumento = s * 0.20
    
novoSal = s + aumento
    
print("Novo salário: R$ %.2f" %(novoSal))
