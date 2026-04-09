lista = []
somatorio = 0
acum = 0

for i in range(10):
    nro = int(input("Digite um número: "))
    lista.append(nro)
    if acum == 0:
        somatorio = (lista[i - 1])
        acum = acum + 1
    else:
        somatorio = (lista[i - 1]) + (lista[i - 2])
    if nro > somatorio:
        print(nro)   

    
