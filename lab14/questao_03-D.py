import time

def contagem_regressiva(tempo):
    while tempo > 0:
        print (tempo)
        tempo -= 1
        time.sleep(1)

print (contagem_regressiva(5))