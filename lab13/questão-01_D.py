import random

numero = random.randint(1, 10)
for i in range(3):
    n = int(input("Adivinhe o número: "))
    if n == numero:
        print ("Correto!")
        break