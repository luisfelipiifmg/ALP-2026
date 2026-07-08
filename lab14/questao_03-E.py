import random

def roleta():
    valor = random.randint(1, 36)
    if valor % 2 == 0:
        return f"{valor}, Preto"
    else:
        return f"{valor}, Vermelho"

print (roleta())
    