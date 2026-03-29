maior = 0
naomaior = 0
n = int(input("Digite um número: "))
while n != -1:
    if n > 10:
        maior = maior + 1
    else: 
        naomaior = naomaior + 1
print(maior)
print(naomaior)
