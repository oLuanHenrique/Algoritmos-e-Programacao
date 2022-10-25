#1761 - Loja Tabajara - Python

valor = 1
compra = 0
while valor != 0:
    valor = float(input())
    compra += valor

valorApagar = float(input())
troco = valorApagar - compra

print("Total da compra: R$%.2f" % compra)
print("Valor pago: R$%.2f" % valorApagar)
print("Troco: R$%.2f" % troco)