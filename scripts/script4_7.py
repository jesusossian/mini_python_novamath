numero = 22
qtd_tentativas = 5
tmp = 1
while (tmp <= qtd_tentativas):
    palpite = int(input("digite um palpite: "))
    if (palpite == numero):
        print("palpite correto")
    elif (palpite > numero):
        print("palpite maior que o número")
    elif (palpite < numero):
        print("palpite menor que o número")
    tmp += 1
