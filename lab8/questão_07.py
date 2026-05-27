degrau = 1
while True:
    print ("Seu degrau: ", degrau)
    passos = int(input("Quantos passos você dará?(Apenas de 1 à 6) ou 0 pra sair "))
    if passos > 6 or passos < 0:
        print ("Número de passos inválido, tente de novo")
        continue
    if passos == 0:
        break
    degrau += passos
    if degrau % 3 == 0:
        print ("Volte 1 degrau! 💀")
        degrau -= 1
        continue
    if degrau % 5 == 0:
        print ("Avance 1 degrau! ✨")
        degrau += 1
        continue
    if degrau % 7 == 0:
        print ("Avance 4 degrau! ✨")
        degrau += 1
        continue
    if degrau % 11 == 0:
        print ("Você pisou num degrau amaldiçoado, agora volte TUDO!!")
        degrau = 1
        continue