# Faça um programa que receba dois valores float : um de altura e
# um de peso, para calcular o IMC. Por fim mostre o resultado.

altura = float(input("qual a altura? "))
peso = float(input("qual o peso? "))
imc = peso/(altura*altura)

print(f"seu imc é: {imc:.2f}")


