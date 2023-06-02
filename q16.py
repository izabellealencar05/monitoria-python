# Faça uma calculadora que receba números inteiros e
# posteriormente a operação a ser feita com esse número
# e então retorne o resultado.

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

print("Escolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Digite o número da operação desejada: "))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if opcao == 1:
    resultado = adicao(num1, num2)
    operacao = "+"
elif opcao == 2:
    resultado = subtracao(num1, num2)
    operacao = "-"
elif opcao == 3:
    resultado = multiplicacao(num1, num2)
    operacao = "*"
elif opcao == 4:
    resultado = divisao(num1, num2)
    operacao = "/"

print(f"Resultado: {num1} {operacao} {num2} = {resultado}")