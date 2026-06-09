jogos = int(input("Quantos jogos o Galo jogou?"))
vitoria = 0
derrota = 0
empate = 0
for n in range(jogos):
    gols_g = int(input("Quantos gols o galo deu? "))
    gols_a = int(input("Quantos gols o outro time fez? "))
    if gols_g > gols_a:
        vitoria += 1
        jogos -= 1
        continue
    if gols_g < gols_a:
        derrota += 1
        jogos -= 1
        continue
    if gols_g == gols_a:
        empate += 1
        jogos -= 1
        continue
print (f'''
Vitórias: {vitoria}
Empates: {empate}
Derrotas: {derrota}
Pontuação: {(vitoria*3) + empate}
''')