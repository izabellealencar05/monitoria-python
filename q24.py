# Criar um lista que ter esses valores ( 20 , 40 ,30 ,10 , 0 )
# faz como que eles virarem uma lista decrescente
# Apaga a posição dois(2) e mostrar o valor apagado
# Inserir o valor dois (2) na posição quatro (4)
# tamanho da lista


lista = [20, 40, 30, 10, 0]
copia = lista.copy()
print('a lista: ', lista)
lista.reverse()
print('o tamanho da lista é:', len(lista))
print('a lista em ordem decrescente é: ', lista)
del copia [2]
print('a lista sem o segundo elemento fica: ', copia)
copia.append(2)
print('adicionando o valor 2 na lista: ', copia)

