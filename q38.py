# Faça um programa que receba 5 valores e faça a soma do primeiro e do terceiro valor,
# no final mostre o resultado na tela.

lista = []

for i in range(5):
    x = int(input('escreva um valor: '))
    lista.append(x)

print(lista)
soma = lista[0]+lista[3]
print('a soma do primeiro valor da lista com o terceiro valor é: ', soma)


