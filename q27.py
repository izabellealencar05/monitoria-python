n1 = int(input("qual número deseja começar: "))
n2 = int(input("deseja ir de quanto em quanto: "))
n3 = int(input("qual número deseja terminar: "))


for count in range(n1, n3+1, n2):
   print(count)