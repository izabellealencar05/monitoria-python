#Faça uma função que aceita 2 variáveis e retorna a multiplicação
def mult(a, b):
    return f'A multiplicaçao entre a e b é: {a*b}'

if __name__ == "__main__":
    a = int(input("valor de a: "))
    b = int(input("valor de b: "))
    print(mult(a, b))