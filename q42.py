# Repita o exercício 1, so que dessa vez você deve utilizar o break (Usando while)

soma = 0
quantidade = 0

while True:
    valor = float(input("Digite um valor (ou -1 para sair): "))
    if valor == -1:
        break
    soma += valor
    quantidade += 1

if quantidade > 0:
    media = soma / quantidade
    print(f"A média dos valores é: {media:.2f}")
else:
    print("Nenhum valor foi inserido.")