entrada = 0
total = 0
pares = 0
cont = 0


while True:
 entrada = int(input("\n\n\tDigite o valor: "))


 cont+=1
 if entrada % 2 == 0: pares+=1
 total += entrada


 print("\n\t"+"*"*40)
 print("\t*"+f" Quantidade de elementos: \t{cont}")
 print("\t*"+f" Soma dos valores: \t\t{total}")
 print("\t*"+f" Media dos valores: \t\t{total/cont:.2f}")
 print("\t*"+f" Total de pares: \t\t\t{(float(pares/cont))*100:.2f}%")
 print("\t"+"*"*40)