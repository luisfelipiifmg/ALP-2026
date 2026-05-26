import random

numero_secreto = (random.randint(1, 10))
chances = 10

while chances > 0:
    num = int(input("Tente adivinhar o número secreto (Você tem 5 chances): "))
    chances -= 1
    if num == chances:
        print ("Você acertou!")
        break
