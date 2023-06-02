# Escrever um programa que solicita ao usuário um conjunto de 10
# valores reais e mostrar a média dos 10 números .(usando só o FOR)
# (dois casa decimal)

soma = 0

for i in range(10):
    numero = float(input("Digite um número real: "))
    soma += numero

media = soma / 10
media_formatada = "{:.2f}".format(media)

print("A média dos números é:", media_formatada)
