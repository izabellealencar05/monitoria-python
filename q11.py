#O professor aplicou a avaliação em sua turma
#e deseja mostrar se o aluno foi aprovado
#(nota maior ou igual a 5) ou reprovado(nota menor que 5).
#Desenvolva o programa que leia a nota do aluno e gere a tela de saída com
#as informações solicitadas.

nota = int(input("qual a nota? "))

if nota >= 5:
    print('aprovado')
else:
    print('reprovado')

