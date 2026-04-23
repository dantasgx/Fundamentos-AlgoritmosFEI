import random

numeros = []

for i in range(100):
    numeros.append(random.randint(0,20))

contagem = {}

for num in numeros:
    if num in contagem:
        contagem[num] +=1
    else:
        contagem[num] = 1

print(contagem)
