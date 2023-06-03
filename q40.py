# Achar o maior e o menor número de uma série de números inteiros
# positivos fornecidos pelo usuário via teclado. O programa deve solicitar
# valores até que o usuário entre com -1. (Usando while e condicionais)

lista = []
x = int(input('Digite um número: '))

while x != -1:
    lista.append(x)
    x = int(input('Digite um número: '))

if lista:
    print('O menor valor da lista é:', min(lista))
    print('O maior valor da lista é:', max(lista))


