#Crie uma função que recebe dois parâmetros e faz a soma, produto,
#divisão e subtração desses parâmetros após isso implemente a aplicação
#dessa função em outro programa e mostro o resultado no segundo programa

def operacao(a, b):
    soma = a + b
    multiplicacao = a * b
    subtracao = a - b
    divisao = a/b
    return f'soma: {soma}, multiplicacao: {multiplicacao}, subtracao: {subtracao}. divisao: {divisao}'
if __name__ == "__main__":
    a = float(input("escreva o valor de A: "))
    b = float(input("escreva o valor de B: "))
    print(operacao(a, b))