# Escreva um algoritmo que solicita ao usuário N notas, calcula e imprime na tela
# do computador a média do aluno. O programa deve continuar solicitando notas até
# que o usuário entre com -1. (Usando while)


soma = 0
quantidade = 0

nota = float(input("digite a nota: "))

while nota != -1:
    soma += nota
    quantidade += 1
    nota = float(input('digite a nota: '))
if quantidade > 0:
    media = soma/quantidade
    print('a media é: ', media)
else: print('nenhuma nota inserida')