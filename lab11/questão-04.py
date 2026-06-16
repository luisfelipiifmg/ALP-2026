import random
import time
pontos_p1 = 0
pontos_p2 = 0
while pontos_p1 < 50 or pontos_p2 < 50:
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    total = dado1 + dado2
    resp_p1 = int(input(f"Jogador 1 ({pontos_p1} pontos): Qual o seu palpite para a soma dos dados? "))
    resp_p2 = int(input(f"Jogador 2 ({pontos_p2} pontos): Qual o seu palpite para a soma dos dados? "))
    if abs(resp_p1 - total) < abs(resp_p2 - total):
        print("Rolando os dados...")
        time.sleep(2)
        print(f'''
        Dado 1: {dado1}
        Dado 2: {dado2}
        JOGADOR 1 GANHA 5 PONTOS!!!''')
        pontos_p1 += 5
        continue
    elif abs(resp_p2 - total) < abs(resp_p1 - total):
        print("Rolando os dados...")
        time.sleep(2)
        print(f'''
        Dado 1: {dado1}
        Dado 2: {dado2}
        JOGADOR 2 GANHA 5 PONTOS!!!''')
        pontos_p2 += 5
        continue
    elif abs(resp_p1 - total) == abs(resp_p2 - total):
        print("Rolando os dados...")
        time.sleep(2)
        print(f'''
        Dado 1: {dado1}
        Dado 2: {dado2}
        EMPATE! Ambos os jogadores ganham 2 pontos''')
        pontos_p1 += 2
        pontos_p2 += 2
        continue
if pontos_p1 > pontos_p2:
    print(PA)
