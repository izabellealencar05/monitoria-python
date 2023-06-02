# Faça um programa que receba 5 valores e Adicionar esses valores
# na lista e depois mostrar a quantidade de valores armazenado na
# lista e imprimir a lista

lista = []

for i in range(5):
    x = int(input('escreva um valor: '))
    lista.append(x)

print('a quantidade de elementos da lista é:', len(lista))
print(lista)



