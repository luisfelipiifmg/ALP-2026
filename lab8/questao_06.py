while True:
    valor = int(input("Quanto você deseja sacar? "))
    notas100 = valor // 100
    valor = valor % 100
    notas50 = valor// 50
    valor = valor % 50
    notas20 = valor // 20
    valor = valor % 20
    if valor == 0:
        print ("Saque realizado com sucesso!")
        break
    print ("Valor inválido, tente novamente")
