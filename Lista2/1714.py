#1714 - Comerciante - Python

precoCompra = float(input())

if (precoCompra<20):
    lucro = precoCompra * 0.45
else:
    lucro = precoCompra * 0.30

valorVenda = precoCompra + lucro
    
print("Valor de venda: R$%.2f" %(valorVenda))