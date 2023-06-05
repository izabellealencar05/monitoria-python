# Criar um lista com 5 numero diferentes
#
# A )Acrescente o valor 3 e 4  na lista
#
# B ) Faça com que eles virem uma lista decrescente
#
# C ) Depois mostre o tamanho da lista
#
# D ) Apaga a primeira posição da lista e coloca o valor 35
#
# E ) Imprimir a lista

lista = [1, 2, 6, 7, 8]
print('lista original: ', lista)
lista.append(3)
lista.append(4)
print('lista com 3 e 4 adicionados', lista)
lista.sort(reverse=True)
print('lista em ordem decrescente', lista)
print('o tamanho da lista é: ', len(lista))
del lista[0]
lista.insert(0, 35)
print(lista)