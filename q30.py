# Faça um programa que receba N números inteiros, e
# todos os números menores ou igual a 0 passem a ser 1 . (usa FOR)

quantidade = int(input('Digite a quantidade de termos: '))
numeros = []
for i in range(quantidade):
    termo = int(input('digite um numero: '))
    numeros.append(max(termo, 1))

for termo in numeros:
    print(termo)

