somatorio = 0

while True:
    entrada = int(input("Digite um número a somar ou 0 pra sair: "))
    if entrada == 0:
        break
    else: 
        somatorio = somatorio + entrada
print( "Somatoria: ", somatorio)