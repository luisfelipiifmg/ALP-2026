import random 
import time
while True:
    prob = random.randint(1, 10)
    pergun = input("Faça uma pergunta e pensarei em uma resposta! ")
    if prob <= 5:
        print ("Deixe-me pensar...")
        time.sleep(2)
        print ("Estou pensando...")
        time.sleep(2)
        print ("JÁ SEI!")
        time.sleep(2)
        print ("SIM!")
        continue
    else:
        print ("Deixe-me pensar...")
        time.sleep(2)
        print ("Estou pensando...")
        time.sleep(2)
        print ("JÁ SEI!")
        time.sleep(2)
        print ("não...")
        break
        
