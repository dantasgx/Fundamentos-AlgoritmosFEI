from math import ceil
altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))


areaBase = 3.1415*raio**2
areaLateral = altura * (2*3.1415*raio)
areaCilindro = areaBase + areaLateral
litro = areaCilindro / 3
lata = ceil (litro / 5)

if lata == 1 :
    valorLata = 50.00
    valorTotal = valorLata*lata
elif lata == 2:
    valorLata = 48.00
    valorTotal = valorLata*lata
elif lata == 3:
    valorLata = 46.00
    valorTotal = valorLata*lata
elif lata > 3:
    valorLata = 45.00
    valorTotal = valorLata*lata

print("altura: ", altura)
print("raio: ", raio)
print("área a ser pintada: %.2f " % areaCilindro)
print("qntd litros necessários: %.2f" % litro)
print("qntd de latas de tinta: ", lata)
print("preço unitário da lata é: ", valorLata)
print("custo total é: ", valorTotal)


