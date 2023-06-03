# Desenvolva o programa que leia vários(N) números e mostre estas informações:
# A) Quantidade de elementos dados ;
# B) Soma dos valores ;
# C) media dos valores ;
# D) porcentagem de números pares ate dois casas decimais
# (( Pode usar o comando While ou For ))

# A) Quantidade de elementos dados ;
lista = []
x = int(input('digite a quantidade de valores: '))
for i in range(x):
     y = int(input('digite um valor: '))
     lista.append(y)

print('a lista é: ', lista)
print('a quantidade de elementos da lista é: ', len(lista))

# B) Soma dos valores ;
print('a soma dos valores da lista é: ', sum(lista))

# C) media dos valores ;
soma = sum(lista)
media = soma/x
print(f'a media dos valores da lista é : {media:.2f}')

# D) porcentagem de números pares ate dois casas decimais
contadordepares = 0
for y in lista:
    if y %2 ==0:
        contadordepares += 1

porcentagempares = (contadordepares/len(lista))* 100
print(f'a porcentagem de pares na lista é: {porcentagempares:.2f}')