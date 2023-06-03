# Uma agência de publicidade quer prestar seus serviços somente para
# a maior companhia, considerando a quantidade de funcionários. Para tal,
# conseguimos um conjunto de dados com o CNPJ (Cadastro Nacional de Pessoa Jurídica)
# e a quantidade de funcionários de várias empresas. Construa o programa que leia esses
# dados de entrada e mostre o CNPJ e a quantidade de funcionários da maior empresa,
# ou seja, da empresa com maior recursos humanos
maiorcnpj =""
maiorqntdfunc = 0
while True:
    cnpj = input('digite o CNPJ ou escreva SAIR: ')
    if cnpj.lower()=="sair":
        print('vc desejou sair do programa')
        break
    qtdfunc = int(input('escreva a quantiade de funcionarios: '))
    if qtdfunc > maiorqntdfunc:
        maiorcnpj = cnpj
        maiorqntdfunc = qtdfunc
    print('a maior empresa é de CNPJ', maiorcnpj, "com", maiorqntdfunc, 'funcionarios')