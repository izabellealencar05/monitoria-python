#Crie um programa que receba três notas de 0 até 10 (faça as validações para aceitar apenas esse intervalo),
#depois faça o cálculo da média aritmética e então mostre a média calculada e também se o aluno passou ou não.
#A escola aceita notas 7 (sete) acima para aprovação.
#Atenção para a indentação do código (inclusive na entrega dos exercícios)

n1 = float(input("qual a sua primeira nota? "))
n2 = float(input("qual a sua segunda nota? "))
n3 = float(input("qual a sua terceira nota? "))

if 0 < n1 <= 10  and 0 < n2 <= 10 and 0 < n3 <= 10:
    media = (n1+n2+n3)/3
    print("sua media foi: ", media)
    if media >= 7:
        print("aprovado")
    else:
        print("reprovado")

else:
    print("nota invalida")



