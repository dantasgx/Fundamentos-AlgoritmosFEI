comp = -99999999999
cont = 0
while cont < 5:
    n = int(input("Digite um número: "))
    if n > comp:
        comp = n
    cont = cont +1
print("O maior número digitado foi: ", comp)
