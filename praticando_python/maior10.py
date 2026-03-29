cont = 0
maior = 0
while cont < 5:
    n = int(input("Digite um número: "))
    if n > 10:
        maior = maior + 1
    cont = cont + 1
print("Números maiores que 0: ", maior)