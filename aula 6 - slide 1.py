# while True:
#    Continuar = str(input("Deseja continuar ? (s/n) : ")).upper()
#    if Continuar == 'S':
#        print("\nVocê decidiu continuar...")
#        continue
#    break

# while  True :
#          Continuar = input("Deseja continuar ? (s/n) : ").lower ()        #.upper()
#          if Continuar == 's' :
#                   print("\nVocê decidiu continuar...")
#          else :
#                   break

#exemplo 1
# '''Escreva um algoritmo que solicita ao usuário N notas,
#  calcula e imprime na tela do computador a média do aluno.
#   O programa deve continuar solicitando notas até que o
#    usuário entre com -1. (Usando while)'''

media = 0
contador = 0
while True:
    n = float(input("digite sua nota: "))
    if n == -1:
        break
    media = media + n
    contador += 1
print(f"sua media é: {media/contador}")
