def soma_digitos(valor):
    v = 10
    soma = 0
    while valor > 0:
        r = valor % v
        soma += r
        valor = (valor - r)/10
    return soma

print(soma_digitos(12345))