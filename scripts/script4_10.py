numero = 22
qtd_tentativas = 5
for t in range(1,qtd_tentativas+1):
    palpite = int(input("digite um palpite: "))
    if (palpite == numero):
        print("palpite correto")
        break
    elif (palpite > numero):
        print("palpite maior que o número")
    elif (palpite < numero):
        print("palpite menor que o número")
