lista = []
parSoma = 0
imparSoma = 0

for i in range(10): 
    nro = int(input("Informe um número: "))
    lista.append(nro);
    if nro % 2 == 0:
        parSoma = parSoma + nro
    else:
        imparSoma = imparSoma + nro

print("A soma dos elementos pares é: ", parSoma)
print("A soma dos elementos ímpares é: ", imparSoma)

