lista = []
maior = -9999999
indice = -1

# laço de repetição para criar a lista com 10 elementos digitados
for i in range(10): 
    nro = int(input("Informe um número: "))
    lista.append(nro);

# laço de repetição para encontrar o maior valor e seu indice
for i in range(len(lista)):
    if lista[i] > maior:
        maior = lista[i]
        indice = i
print(maior)
print(indice)
