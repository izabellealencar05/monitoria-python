#Crie um programa que receba duas notas e informe se a pessoa passou ou não.
#Considere que o usuário irá informar uma nota de 0 à 10 e que média a partir
#de 5 leva o aluno a aprovação

x = float(input("Qual a sua nota? "))
y = float(input("Qual a segunda nota: "))
media = (x + y)/2
if media >= 5:
    print("Parabéns, vc foi aprovado")
elif media < 5:
    print("Vc foi reprovado")
