import random

numero_secreto = (random.randint(1, 10))
chances = 5

while chances > 0:
    num = int(input("Tente adivinhar o número secreto (Você tem 5 chances): "))
    chances -= 1
    if num > numero_secreto:
        print ("Menor")
    elif num < numero_secreto:
        print ("Maior")
    elif num == numero_secreto:
        print ("Você acertou!")
        break