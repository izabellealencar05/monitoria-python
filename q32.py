#Faça um programa que receba 5 valores e me mostre o somatório dos valores.
lista = []
for i in range(5):
    valor = int(input('digite um valor: '))
    lista.append(valor)
print(lista)
print(sum(lista))