#Escreva um algoritmo que solicita ao usuário um valor N inteiro positivo e imprime na tela do computador todos os número inteiros de 0 até N digitado. (Usando for)
n = int(input("Digite um número: "))

for count in range(0, n+1, 1):
   print(count)