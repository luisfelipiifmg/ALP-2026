cont = 0
soma = 0
while True:
    n = int(input("Seu número (0 para encerrar): "))
    if n < 0:
        print ("Número inválido, valor deve ser positivo")
        continue
    if n == 0:
        print (soma, cont, (soma / cont))
        break
    soma += n
    cont += 1
