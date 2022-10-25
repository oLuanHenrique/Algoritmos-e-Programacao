#1713 - Salário 02 - Python

a = float(input())
b = float(input())

salarioBruto = a * b
inss = salarioBruto * 0.08
ir = salarioBruto * 0.11
sindicato = salarioBruto * 0.05
imposto = inss + ir + sindicato
salarioLiquido = salarioBruto - imposto

print("Salário bruto: R$ %.2f\n Imposto: R$ %.2f\n INSS: R$ %.2f\n Sindicato: R$ %.2f\n Líquido: R$ %.2f" %(salarioBruto,ir,inss,sindicato,salarioLiquido)