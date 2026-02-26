anoAtual = int(input("Digite o ano atual: "))
anoNasc= int(input("Digite seu ano de nascimento "))
idade = anoAtual - anoNasc

if idade >= 18:
    print("Você pode tirar a CNH!!")
if idade < 18:
    print("Você ainda não pode tirar a CNH ):")