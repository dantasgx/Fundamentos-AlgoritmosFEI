qtde = 0
acum = 0
n = int(input("Digite um número: "))
while n != 0:
    qtde = qtde+1
    acum = acum + n
    n = int(input("Digite um número: "))
print("Soma: ", acum)
print("Quantidade: ", qtde)
