ganhoHora = float(input("Escreva o valor que você ganha por hora: "))
horasMes = int(input("Escreva o número de horas trabalhadas no mês: "))
salarioBruto = ganhoHora * horasMes
ir = salarioBruto*0.11
inss = salarioBruto*0.08
sindicato = salarioBruto*0.05
salarioLiquido = salarioBruto - ir - inss - sindicato
print("O salario liquido é de %.2f " % salarioLiquido)