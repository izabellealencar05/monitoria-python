# Faça um programa que receba 5 valores e Adicionar esses valores na lista e
# depois mostrar a quantidade de valores armazenado na lista e imprimir a lista

lista = []
for i in range(5):
    x = int(input('digite um valor: '))
    lista.append(x)
print('a lista criada é: ', lista)
print('o tamanho da lista é: ', len(lista))


