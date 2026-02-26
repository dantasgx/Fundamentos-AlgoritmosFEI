altura = float(input("Digite a sua altura (ex: 1.70): "))
sexo = input("Informe o seu sexo: (m para masculino e f para feminino) ")

if sexo == "m":
    pesoIdeal = (72.7 * altura) - 58
elif sexo == "f":
    pesoIdeal = (62.1 * altura) - 44.7
else:
    print("Você não digitou os valores corretamente")
print ("Seu peso ideal é: %.1f " % pesoIdeal)