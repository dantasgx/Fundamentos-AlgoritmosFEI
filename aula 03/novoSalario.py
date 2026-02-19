salario = float(input("Digite o seu salário: "))
if salario > 1250:
    aumento = salario*1.10
    print("Seu novo salário é de R$ %.2f" % aumento)
else:
    aumento = salario*1.15
    print("Seu novo salário é de R$ %.2f " % aumento)

