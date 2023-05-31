# Crie um programa que receba duas notas e informe se a pessoa passou ou não.
# Considere que o usuário irá informar uma nota de 0 à 10 e que média a partir
# de 5 leva o aluno a aprovação

n1 = int(input('digite a primeira nota: '))
n2 = int(input('digite a segunda nota: '))
media = (n1 + n2)/2

if 0 < media <= 4.9:
    print('reprovado')
else:
    print('aprovado')