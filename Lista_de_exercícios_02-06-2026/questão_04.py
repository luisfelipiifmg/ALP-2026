while True:
    x = int(input("Primeiro número: "))
    y = int(input("Segundo número: "))
    if x > y:
        print ("O maior número é", x)
        break
    if y > x:
        print ("O maior número é", y)
        break
    if x == y:
        print ("Ambos são iguais, tente novamente")
        continue