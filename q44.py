maior_nota = -1
frequencia_maior_nota = 0
soma_notas = 0
quantidade_notas = 0
quantidade_aprovados = 0
quantidade_reprovados = 0

primeira_nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
if primeira_nota == -1:
    print("Nenhuma nota foi inserida.")
else:
    while True:
        quantidade_notas += 1
        soma_notas += primeira_nota

        if primeira_nota >= 5:
            quantidade_aprovados += 1
        else:
            quantidade_reprovados += 1

        if primeira_nota > maior_nota:
            maior_nota = primeira_nota
            frequencia_maior_nota = 1
        elif primeira_nota == maior_nota:
            frequencia_maior_nota += 1

        primeira_nota = float(input("Digite a nota do aluno (ou -1 para sair): "))
        if primeira_nota == -1:
            break

    media_turma = soma_notas / quantidade_notas

    print("Quantidade de notas digitadas:", quantidade_notas)
    print("Média da turma:", media_turma)
    print("Quantidade de alunos aprovados:", quantidade_aprovados)
    print("Quantidade de alunos reprovados:", quantidade_reprovados)
    print("Maior nota:", maior_nota)
    print("Frequência da maior nota:", frequencia_maior_nota)