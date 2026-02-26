preco = float(input("Digite o preço do produto: "))
codigo = float(input("Digite o código de origem do produto: "))

if codigo == 1:
    procedencia = "Sul"
else:
    if codigo == 2:
        procedencia = "Norte"
    else:
        if codigo == 3:
            procedencia = "Leste"
        else:
            if codigo == 4:
                procedencia = "Oeste"
            else:
                if codigo == 5 or codigo == 6:
                    procedencia = "Nordeste"
                else:
                    if codigo == 7 or codigo == 8 or codigo == 9:
                        procedencia = "Sudeste"
                    else:
                        if codigo >= 10 and codigo <= 20:
                            procedencia = "Centro-Oeste"
                        else:
                            if codigo >= 25 and codigo <= 30:
                                procedencia = "Noroeste"
                            else:
                                procedencia = "Importado"
print ("A origem do produto é: ", procedencia)
print("O preço do produto é: R$ %.2f "% preco)


