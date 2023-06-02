#Faça um programa que receba N números inteiros, e todos os
# números menores ou igual a 0 passem a ser 1 . (usa FOR)

n = int(input('escreva a qunatidade de numeros: '))
numeros = []
for i in range(n):
    numero = int(input('digite um numero: '))
    numeros.append(numero)

for i in range(n):
    if numeros[i] <= 0:
        numeros[i] == 1

for numero in numeros:
    print(numero)