# Escreva um algoritmo que solicita ao usuário N números inteiros,
# calcule e imprima na tela do computador a média(duas casas decimais)
# do aluno.(Usando FOR)

quantidade = int(input('escreva a quantidade de provas: '))
soma = 0

for i in range(quantidade):
    termo = int(input('escreva sua nota: '))
    soma += termo

media = soma/quantidade
print(f'a media das notas é: {media:.2f}')