pos = 0
neg = 0
acum = 0

while acum < 5:
    n = int(input("Digite um número positivo ou negativo: "))
    if n >= 0:
        pos = pos + 1
    else:
        neg = neg + 1
    acum = acum + 1
print("A quantidade de números positivos é: ", pos)
print("A quantidade de números negativos é: ",neg)    