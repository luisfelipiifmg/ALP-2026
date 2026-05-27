soma = 0
while True:
    num = int(input("Seu número: "))
    if num < 0:
        continue
    soma += num
    if soma >= 100:
        print ("Sua soma resultou em", soma)
        break