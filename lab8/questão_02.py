cont = 5
while cont > 0: 
    num = int(input("Digite um número inteiro: "))
    cont -= 1
    if num % 2 == 0: 
        continue
    print(f'{num} é um número ímpar')

## O trecho do código que printa se o número do input é impar é pulado
## se o número que for colocado for par, mas o trecho é printado normalmente
## se o número for impar
