#Faça um programa que receba dois valores float : um de altura e um de peso,
# para calcular o IMC. Por fim mostre o resultado.
#peso/altura^2
altura = float(input("digite sua altura: "))
peso = float(input("digite seu peso: "))
print(f"seu imc é: {peso/altura*altura}")