cont = 0 
maior = -999999
while cont < 6:
    n = int(input("Digite um número: "))
    if n > maior:
        maior = n
    cont = cont + 1

print("O maior número é: ", maior)


