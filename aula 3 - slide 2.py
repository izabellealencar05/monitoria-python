#Faça uma função que receba uma variável e mostre na tela se ele for múltiplo de 2

def e_mult_2(a):
    if a % 2 == 0:
        return "o numero é multiplo de 2"
    else:
        return "nao é multiplo de 2"
if __name__=='__main__':
    a = int(input("digite um numero: "))
    print(e_mult_2(a))