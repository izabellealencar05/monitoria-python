# Receba (input) o valor de um salário e mostre
# o quanto deve ser depositado de FGTS (8% do valor salário)
# para este salário informado
# # fgts = (salário * 8)  / 100
# # fgts = salário * 0.08
# faz como que só mostra até uma casas decimais.

salario = float(input("qual o salario: "))
fgts = (salario*8)/100

print(f"fgts: {fgts:.2f}")
print(f"salario: {salario - fgts:.2f}")


