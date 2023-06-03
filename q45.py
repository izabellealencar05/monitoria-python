# Desenvolva um programa que recebe N números inteiros e retorna o
# maior deles. Se os números forem iguais, retorne um deles.(usando while )

n = int(input('digite a quantidade de numeros: '))
maiornumero = int(input('digite um numero: '))
n -= 1

while n > 0:
    numero = int(input('digite um numero: '))

    if numero > maiornumero:
        maiornumero = numero
    n -= 1

print('o maior numero é: ', maiornumero)
