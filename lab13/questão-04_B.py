import random

for i in range(5):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    diferenca = abs(dado2 - dado1)
    if diferenca == 0:
        break