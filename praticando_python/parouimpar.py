par = 0
impar = 0
cont = 0
while cont < 5:
    n = int(input("Digite um número: "))
    if n % 2 == 0:
        par = par + 1
    else: 
        impar = impar + 1
    cont = cont + 1
print("Pares: ", par)
print("Ímpares: ", impar)