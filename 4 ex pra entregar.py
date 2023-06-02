# Desenvolva um gerador de tabuada, capaz de gerar a tabuada
# de qualquer número inteiro entre 1 a 10. O usuário deve informar
# de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#
# A) Faça uma tabuada usando FOR dentro de um WHILE.
# B) Faça um código, usando for , que mostre todas as tabuadas(1 até 10).


#A
# numero = int(input("Digite um número para ver a tabuada: "))
#
# while numero < 1 or numero > 10:
#     print("Número inválido. Digite um número entre 1 e 10.")
#     numero = int(input("Digite um número para ver a tabuada: "))
#
# for i in range(1, 11):
#     resultado = numero * i
#     print("{} x {} = {}".format(numero, i, resultado))

#B
for numero in range(1, 11):

    print("Tabuada do", numero)
    print("-------------")
    for i in range(1, 11):
        resultado = numero * i
        print("{} x {} = {}".format(numero, i, resultado))
    print()