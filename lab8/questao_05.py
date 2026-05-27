soma = 0
while True:  
    num = int(input(('''
    Cardápio:
    1. Açaí 300ml - R$ 12
    2. Mousse - R$ 6,50
    3. Salada de frutas - R$ 10
    4. Fechar a conta
    ''')))
    if num == 1:
        soma += 12
        print ("Mais alguma coisa?")
    if num == 2:
        soma += 6.50
        print ("Mais alguma coisa?")
    if num == 3:
        soma += 10
        print ("Mais alguma coisa?")
    if num == 4: 
        print ("A sua conta é de R$", (soma))
        break
    if num > 4 or num < 1:
        print ("Número inválido, tente novamente")
        continue

