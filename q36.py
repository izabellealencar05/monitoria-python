# Faça um programa que receba 5 valores e coloque-os em uma lista. Após isso calcule a média dessa lista

lista = []
soma = 0
for i in range(5):
    x = int(input('digite um valor: '))
    soma += x
    lista.append(x)
print('a lista: ', lista)
media = soma/5
print(f'a media dos valores inseridos é: {media:.2f}')
