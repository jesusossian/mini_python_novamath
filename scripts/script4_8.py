numero = 22
qtd_tentativas = 5
tmp = 1
while (tmp < qtd_tentativas+1):
    palpite = int(input("digite um palpite: "))
    if (palpite == numero):
        print("palpite correto")
        break
    elif (palpite > numero):
        print("palpite maior que o número")
    elif (palpite < numero):
        print("palpite menor que o número")
    tmp += 1
