dicionario = {
    'alpha': 1,
    'bravo': 2,
    'charlie': 1,
    'delta': 3,
    'echo': 1
}

print("Dicionário: ")
print(dicionario)

resultado1 = []
resultado3 = []
resultado4 = []

for chave, valor in dicionario.items():
    if valor == 1:
        resultado1.append(chave)
    elif valor == 3:
        resultado3.append(chave)
    elif valor == 4:
        resultado4.append(chave)

print("Procurando chaves com valor 1")
print(resultado1)
print("Procurando chaves com valor 3")
print(resultado3)
print("Procurando chaves com valor 4")
print(resultado4)