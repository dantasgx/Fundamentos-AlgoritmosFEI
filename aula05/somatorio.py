cont = 0
acum = 0

while cont < 10:
    n = int(input("Digite um número: "))
    cont = cont + 1
    acum = n + acum

print("A somatória dos 10 números é: ", acum)