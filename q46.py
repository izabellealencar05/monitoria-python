maior = float('-inf') # 10000000000000
menor = float('inf') # -10000000000000
print("Parar sair digita Zero(0)")
while True:
   numero = int(input("Digite um valor : "))
   if numero == 0:
       break
   else:
       if numero > maior:
           maior = numero
       elif numero < menor:
           menor = numero


print("\tO numero e maior :", maior)
print("\tO numero e menor :", menor)