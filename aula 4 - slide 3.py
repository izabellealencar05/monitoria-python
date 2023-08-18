#Escreva um algoritmo que solicita ao usuário N números inteiros, calcule e imprima na tela do computador a média(duas casas decimais) do aluno.
soma = 0
x = int(input("digite a qntd de provas: "))
for media in range(x):
    nota = float(input("digite as notas: "))
    soma = soma + nota
media = soma /x
print(f'{media:.2f}')
(ctrl) + (/)
