#1733 - Salário condicional - Python

nome = input()
horaExtra = float(input())

salarioMinimo = 1192.40
valorHoraExtra = 10

salarioHoraExtra = horaExtra * valorHoraExtra
salarioBruto = 3 * salarioMinimo + salarioHoraExtra

if salarioBruto>2000:
    descontoINSS = salarioBruto * 0.12
else:
    descontoINSS = salarioBruto * 0.05
    
if salarioBruto>2500:
    descontoIR = salarioBruto * 0.2
else:
    descontoIR = 0

descontos = descontoINSS + descontoIR
salarioLiquido = salarioBruto - descontos
print("Nome:%s"%(nome))
print("Salário bruto: R$%.2f"%(salarioBruto))
print("Salário líquido: R$%.2f"%(salarioLiquido))
