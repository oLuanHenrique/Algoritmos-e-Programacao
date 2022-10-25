#1734 - Fatorial - Python

var = int(input())

contador = 2
resultado = 1 
while contador <= var:
    resultado = resultado * contador
    contador = contador + 1 
    
print("%i! = %i" %(var,resultado))