# Desenvolva o programa que leia vários(N) números digitados e
# mostre estas informações:
#
# A) Quantidade de elementos dados ;
#
# B) Soma dos valores ;
#
# C) media dos valores ;
#
# D) porcentagem(ate duas casas decimais ) de números pares ;
#
# (( Pode usar o comando While ou For ))

lista = []
count = 0
x = int(input('digite quantos elementos: '))
for i in range(x):
    n = int(input('digite um numero: '))
    lista.append(n)
    if n % 2 == 0:
        count += 1
print('a quantidade de elementos da lista é: ', len(lista))
print('a soma dos elementos é: ', sum(lista))
media = sum(lista)/ len(lista)
print(f'a media da lista é:{media:.2f}')
porcentagem = (count/len(lista))*100
print(f'porcentagem de pares: {porcentagem:.2f}%')

