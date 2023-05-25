#Faça um programa que receba N números inteiros, e todos os números menores ou igual a 0 passem a ser 1 . (usa FOR)
n = int(input("digite a qntd de vezes: "))
for numero in range(0, n):
    x = float(input("digite um numero: "))
    if x <= 0:
        print(1)
    else:
        print(n)