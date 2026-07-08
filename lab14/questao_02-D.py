def calculadora(x, y, sinal):
    if sinal == '+':
        return x + y
    elif sinal == "-":
        return x - y
    elif sinal == "*":
        return x*y
    elif sinal == "/":
        return x/y

print (calculadora(100, 2, "/"))