cont = 0
soma = 0
n = -9999999999
while n != 0:
    n = int(input("Digite um número: "))
    if n == 0:
        break
    cont = cont + 1
    soma = n + soma
    media = soma / cont 

print("Quantidade de números digitados: ", cont)
print("Soma dos números digitados: ", soma)
print("Média dos números digitados: %.2f " % media)