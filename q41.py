# Faça um programa que receba N valores e após isso calcule a média desses valores. (Usando while)
# obs: não use o break

soma = 0
quantidade = 0

x = int(input('digite a quantidade de valores: '))
while x > 0:
    y = int(input('digite um valor: '))
    soma += y
    quantidade += 1
    x -= 1

if quantidade > 0:
    media = soma / quantidade
    print('a media dos valores é: ', media)
