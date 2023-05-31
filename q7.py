# Crie um programa que receba três notas de 0 até 10
# (faça as validações para aceitar apenas esse intervalo),
# depois faça o cálculo da média aritmética e então mostre
# a média calculada e também se o aluno passou ou não.
# A escola aceita notas 7 (sete) acima para aprovação.
# Atenção para a indentação do código (inclusive na entrega dos exercícios)

n1 = int(input('digite a primeira nota: '))
n2 = int(input('digite a segunda nota: '))
n3 = int(input('digite a terceira nota: '))
media = (n1+n2+n3)/3


if 0 < n1 <= 10 and 0 <n2 <= 10 and 0 < n3 <= 10:
    print("media: ", media)
    if media >= 7:
        print("aluno aprovado! ")
    else:
        print("aluno reprovado!")

