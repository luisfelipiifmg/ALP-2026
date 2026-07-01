import datetime

hoje = datetime.datetime.now()
resposta = input('Incluir ano? (s/n) ')
if resposta == "s":
    print(f"{hoje.day}/{hoje.month}/{hoje.year}")
else:
    print(f"{hoje.day}/{hoje.month}")