import random

def lancaDados ():
    dado1 = (random.randint(1,6))
    dado2 = (random.randint(1,6))
    somatorio = dado1 + dado2
    return somatorio

numeros = []

for i in range(0, 1000):
    numeros.append(lancaDados())
    
contagem = {}

for num in numeros:
    if num in contagem:
        contagem[num] +=1
    else:
        contagem[num] = 1

print(contagem)

