# Escrever um programa que solicita ao usuário um conjunto de 10
# valores reais e mostrar a média dos 10 números .(usando só o FOR)
# (dois casa decimal)

soma = 0
for i in range (10):
    numero = int(input('digite um termo: '))
    soma += numero
    media = soma/10
print(f'a media dos termos é: {media:.2f}')






