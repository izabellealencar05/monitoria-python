# Crie uma variação do programa anterior, porém com os seguintes requisitos
# adicionais: Calcule uma média ponderada: Peso da Nota 1 é 1, Peso da Nota 2
# é 1.5 e Peso da Nota 3 é 2. Ao invés de mostrar se o aluno foi aprovado ou
# não com base na média ponderada mostre uma menção de SR, II, MI, MM, MS ou SS,
# conforme a média ponderada e usando a escala:

n1 = int(input('digite a primeira nota: '))
n2 = int(input('digite a segunda nota: '))
n3 = int(input('digite a terceira nota: '))
media = ((n1*1)+(n2+1.5)+(n3*2))/4.5

if 0 < n1 <= 10 and 0 <n2 <= 10 and 0 < n3 <= 10:
    if 0 == media:
        print('SR')
    elif 0 < media < 1.9:
        print('II')
    elif 2 < media < 4.9:
        print('MI')
    elif 5 < media < 6.9:
        print('MM')
    elif 7 < media < 8.9:
        print("MS")
    else:
        print('SS')
else:
    print("nota invalida")


