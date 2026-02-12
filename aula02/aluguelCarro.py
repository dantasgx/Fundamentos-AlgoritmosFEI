kmpercorridos = float(input("Informe a quantidade de km percorridos pelo carro: "))
diasAluguel = int(input("Informe a quantidade de dias que o carro foi alugado: "))
valorTotal = (diasAluguel * 60.00) + (kmpercorridos * 0.15)
print("O total a ser pago é de R$ %.2f" % valorTotal)