#Receba (input) o valor de um salário e mostre o quanto deve ser
#depositado de FGTS (8% do valor salário) para este salário informado
#fgts = salário * 0.08

salario = float(input("qual o seu salario? "))
print(f"o fgts é: {salario * 0.08}")
print(f"seu salario dps do fgts é: {salario -(salario * 0.08):.2f}")



