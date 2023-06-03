# Criar um lista que ter esses valores ( 5 , 1, 3 ,4 ,6 , 7 , 0)
# A ) faz como que eles virarem uma lista decrescente
# B ) Acrescente o valor 2 e 4  na lista
# C ) Depois mostra o tamanho da lista
# D ) fala a posição do valor 5
# E ) Quantidade do valor 4
# F ) Apagar na lista a posição dois e colocar o valor 10
# G ) Imprimir a lista

lista = [5, 1, 3, 4, 6, 7, 8]
print('lista original: ', lista)

'''A ) faz como que eles virarem uma lista decrescente'''
lista.sort(reverse=True)
print('a lista em ordem decrescente é: ', lista)

# B ) Acrescente o valor 2 e 4  na lista
lista.append(2)
lista.append(4)
print('a lista com 2 e 4 inseridos: ', lista)

# C ) Depois mostra o tamanho da lista
print('o tamanho da lista é: ', len(lista))

# D ) fala a posição do valor 5
numero = 5
posicao = lista.index(numero)
print('a posicao do numero 5 na lista é: ', posicao)

# E ) Quantidade do valor 4
quantidade = lista.count(4)
print('a quantidade de vezes que o numero 4 aparece na lista é: ', quantidade)

# F ) Apagar na lista a posição dois e colocar o valor 10
del lista[2]
lista.insert(2, 10)
print('a lista com o 10 inserido na 2 posiçao, tendo sido retirado o segundo elemento: ', lista)

# G ) Imprimir a lista
print('resultado final da lista: ', lista)

