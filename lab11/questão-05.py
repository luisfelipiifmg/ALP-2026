import random
digito_1 = random.randint(0, 9)
digito_2 = random.randint(0, 9)
digito_3 = random.randint(0, 9)
termo1 = 0
termo2 = 0
termo3 = 0
for chance in range(10):
    print(digito_1, digito_2, digito_3)
    adivinha_1 = int(input("Qual é o primeiro digito? "))
    adivinha_2 = int(input("Qual é o segundo digito? "))
    adivinha_3 = int(input("Qual é o terceiro digito? "))
    if adivinha_1 == digito_1:
        termo1 = "+"
    elif adivinha_1 == digito_2 or adivinha_1 == digito_3:
        termo1 = "!"
    else:
        termo1 = "_"

    if adivinha_2 == digito_2:
        termo2 = "+"
    elif adivinha_2 == digito_1 or adivinha_2 == digito_3:
        termo2 = "!"
    else:
        termo2 = "_"

    if adivinha_3 == digito_3:
        termo3 = "+"
    elif adivinha_3 == digito_1 or adivinha_3 == digito_2:
        termo3 = "!"
    else:
        termo3 = "_"
    print (termo1, termo2, termo3)

    if termo1 == "+" and termo2 == "+" and termo3 == "+":
        print ("Parabéns, você acertou!")
        break
print ("Que pena, você errou, tente novamente depois!")
