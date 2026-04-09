lista = []
n = int(input("Digite a quantidade de números: "))
for i in range(0, n):
    nro = int(input("Informe um número: "))
    lista.append(nro)
while n > 0:
    print(lista[n-1])
    n = n-1

