# Crie um programa que receba um valor e se esse valor for
#     inferior a um salário mínimo(1200) informe que o salário
#     está fora da legislação e se for negativo ou zero informe
#     que o salário está invalido (usa if e se for necessário pode
#     usar elif e else ).

salario = float(input('escreva o salario: '))

if 1 < salario < 1200:
    print('voce esta fora da legislação!')
elif salario <= 0:
    print('salario invalido!')
else:
    print('seu salario esta de acordo com a legislação!')