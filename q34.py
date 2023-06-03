# Criar um lista que ter esses valores ( 20 , 40 ,30 ,10 , 0 )
# faz como que eles virarem uma lista decrescente
# Apaga a posição dois(2) e mostrar o valor apagado
# Inserir o valor dois (2) na posição quatro (4)
# tamanho da lista

lista = [20, 40, 30, 10, 0]
lista.sort(reverse=True)
print('a lista em ordem decrescente é: ', lista)
valorremovido = lista[2]
del lista [2]
print('a lista sem o segundo valor: ', lista)
print('o valor removido foi: ', valorremovido)
lista.insert(4, 2)
print('lista com o 2 inserido na 4 posição: ', lista)
print('o tamanho da lista é: ', len(lista))