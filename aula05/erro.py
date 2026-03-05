n = int(input("Digite um número de 0 a 10: "))

while n < 0 or n > 10:
    print("Número Inválido")
    n = int(input("Digite um número de 0 a 10 por favor: "))

print("Número Aceito")
print("O número escolhido foi: ", n)