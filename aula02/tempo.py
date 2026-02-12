dias = int(input("Escreva a quantidade de dias: "))
horas = int(input("Escreva a quantidade de horas: "))
minutos = int(input("Escreva a quantidade de minutos: "))
segundos = int(input("Escreva a quantidade de segundos: "))
tempoTotal = (dias*24*60*60) + (horas*60*60) + (minutos*60) + segundos
print("O tempo total é de ", tempoTotal ,"segundos")