#Escreva um algoritmo que solicita ao usuário N números inteiros,
# calcule e imprima na tela do computador a média(duas casas decimais) do aluno

n = int(input('digite a quantidade de numeros: '))
soma = 0

for i in range(n):
    numero = int(input('digite um numero: '))
    soma += numero

media = soma/n
media = round(media, 2)

print(f'a media é: {media}')