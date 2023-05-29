# #O professor aplicou a avaliação em sua turma e
# deseja selecionar a maior nota e sua respectiva
# frequência, ou seja, a quantidade de alunos que
# conseguiu a maior nota. Desenvolva o programa que
# leia a nota dos alunos e gere a tela de saída com
# as informações solicitadas.

maior = 0
menor = 0
while True:
    x = int(input("digite um numero: "))
    if x == -1:
        break
    if x > maior:
        maior = x
    if x < menor:
        menor = x
print(f"maior: {maior} menor: {menor}")