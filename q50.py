valores = list(map(str ,input("Digite o CNPJ e o Num de Funcionarios: ").split(' ')))
impares = []
print(valores)

for x in range(len(valores)):
   if (x%2!=0):
       impares.append(valores[x])
       maior = max(impares)

pos_cnpj_maior = valores.index(maior)-1
print(f"CNPj:{valores[pos_cnpj_maior]}, Num de Funcionários: {maior}")
