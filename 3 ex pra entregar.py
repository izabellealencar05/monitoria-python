# Desenvolva o programa que leia vários(N) números e mostre estas informações:
# A) Quantidade de elementos dados ;
# B) Soma dos valores ;
# C) media dos valores ;
# D) porcentagem de números pares ate dois casas decimais
# (( Pode usar o comando While ou For ))


numeros = []


while True:
    n = int(input('Digite um número (0 para sair): '))
    if n == 0:
        break
    numeros.append(n)

# A) Quantidade de elementos dados
qntd = len(numeros)
print('A quantidade de números é:', qntd)

# B) Soma dos valores
soma = sum(numeros)
print("A soma dos valores é:", soma)

# C) Média dos valores
media = soma / qntd
print("A média dos valores é:", media)

# D) Porcentagem de números pares
pares = sum(1 for num in numeros if num % 2 == 0)
porcentagem = (pares / qntd) * 100
print("A porcentagem de números pares da lista é: {:.2f}%".format(porcentagem))