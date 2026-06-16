while True:
    resp = input("Você quer saber como manter uma pessoa ingênua ocupada por horas? S/N" )
    if resp == "s" or resp == "S" or resp == "sim" or resp == "SIM":
        continue
    elif resp == "n" or resp == "não" or resp == "N" or resp == "NÃO":
        print ("Obrigado, tenha um bom dia!")
        break
    else:
        print (resp, "não é uma resposta válida de Sim/Não")
        continue