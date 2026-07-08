def ola(nome, genero):
    if genero == "neutro":
        return f"Olá {nome}, boas vindas!"
    elif genero == "feminino":
        return f"Olá {nome}, bem vinda!"
    elif genero == "masculino":
        return f"Olá {nome}, bem vindo!"

print (ola("Leo", "masculino"))
