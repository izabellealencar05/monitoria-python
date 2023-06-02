# Criar um lista que ter esses valores ( 5 , 1, 3 ,4 ,6 , 7 , 0)
# A ) faz como que eles virarem uma lista decrescente
# B ) Acrescente o valor 2 e 4  na lista
# C ) Depois mostra o tamanho da lista
# D ) fala a posição do valor 5
# E ) Quantidade do valor 4
# F ) Apagar na lista a posição dois e colocar o valor 10
# G ) Imprimir a lista

lista = [5, 1, 3, 4, 6, 7]
print(lista)
lista.reverse()
print('lista em ordem decrescente: ', lista)
lista.append(2)
lista.append(4)
print('lista com o dois acrescentado: ', lista)
print('o tamanho da lista é', len(lista))

