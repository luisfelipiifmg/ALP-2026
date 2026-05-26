## a)

N = int(input("Quantos números quer digitar?"))
contador = N
impares = 0

while contador != 0:
    num = int(input("Digite um número: "))
    if num % 2 != 0:
        impares += 1
    contador -= 1
## O número do contador nunca mudava, ou seja, era um looping infinito de inputs

print(f"Quantidade de ímpares: {impares}")

## b)

soma = 0
contador = 0
while contador < 10: 
    num = int(input("Digite um número para somar: "))
    soma += num
    contador += 1
print (soma)

## Não possuia um contador, o while utilizava da própria soma dos números do input como contador
## O input coletava 11 números ao invés de 10
## O programa não imprimia o resultado da soma

## c)

maior = float('-inf')
soma = 0
while soma <= 10: 
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
    soma += 1
print('O maior número é', maior)

## A variável "soma" (que existia no while) não havia um valor settado, logo não resultaria em nada
## Não existia nada para parar o while (mesmo que a variável de soma tivesse um valor fixo antes)
## Maior era igual à infinito, e não à infinito negativo, logo não existia valor maior que a variável maior, pois ela equivalia à infinito