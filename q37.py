# Faça um programa que vai ler 5 números e colocar em uma lista.
# Após isso, esse programa vai reorganizar a lista na ordem numérica.

lista = []
for i in range(5):
    x = int(input('escreva um numero: '))
    lista.append(x)
print('a lista original: ', lista)
print('a lista organizada em ordem crescente: ', sorted(lista))
