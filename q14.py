#Faça uma função que receba uma variável e mostre na tela se ele
# for múltiplo de 2

def mult (a):
    if a%2 == 0:
        print('o numero é multiplo de 2')
    else:
        print('o numero não é multiplo de 2')

if __name__ == '__main__':
    a = int(input('digite o valor de A: '))
    mult(a)