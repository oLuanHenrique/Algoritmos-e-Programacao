#1019 - Conversão de Tempo

valint = int(input())

horas = valint // 60  //60
valint = valint - (horas * 60 * 60)

minutos = valint // 60

segundo = valint % 60

print("%i:%i:%i"%(horas,minutos,segundo))
