anoNasc = int(input("Digite o ano do seu nascimento: "))
idade = 2026 - anoNasc

if idade >= 16:
    print ("Você pode votar!")
else:
    print ("Você não tem idade pra votar!")
if idade >= 18:
    print ("Você pode tirar a CNH!!")
else:
    print("Você não tem idade pra tirar a CNH!")
