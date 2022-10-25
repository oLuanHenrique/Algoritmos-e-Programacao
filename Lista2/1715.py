#1715 - Loja - Python

a = int(input())
b = float(input())

cc = b
f = b - (b * 0.13)
p = b- (b * 0.07)


if a == 1:
    print("Valor total a ser pago: R$ %.2f" %(cc))
elif a== 2:
    print("Valor total a ser pago: R$ %.2f" %(f))
elif a == 3:
    print("Valor total a ser pago: R$ %.2f" %(p))
else:
    print("OPÇÃO INVÁLIDA!")