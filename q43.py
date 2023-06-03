# O professor aplicou a avaliação em sua turma e deseja selecionar a maior nota e
# sua respectiva frequência, ou seja, a quantidade de alunos que conseguiu a maior
# nota. Desenvolva o programa que leia a nota dos alunos e gere a tela de saída com
# as informações solicitadas.



maior_nota = -1
frequencia_maior_nota = 0

while True:
    nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
    if nota == -1:
        break

    if nota > maior_nota:
        maior_nota = nota
        frequencia_maior_nota = 1
    elif nota == maior_nota:
        frequencia_maior_nota += 1

if frequencia_maior_nota > 0:
    print(f"A maior nota é {maior_nota} e foi obtida por {frequencia_maior_nota} aluno(s).")
else:
    print("Nenhuma nota foi inserida.")