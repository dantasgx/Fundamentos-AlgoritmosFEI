n = int(input("Digite o tamanho do tabuleiro: "))

for i in range(n):
    for j in range (n):
        if j % 2 == 0:
            if (i + j) % 2 == 0:
                print("$", end=" ")
            else:
                print("&", end=" ")
        else:
            if (i + j) % 2 == 0:
                print("%", end=" ")
            else:
                print("#", end=" ")
    print()