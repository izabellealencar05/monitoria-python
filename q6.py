# Faça um programa que retorna a hora que for
# digitada e cumprimente de acordo com o horário.

hora = float(input("que hora sao? "))

if 0 <= hora < 6:
    print("é madrugada")
elif 6 <= hora < 12:
    print("é dia")
elif 12 <= hora < 18:
    print("é tarde")
elif 18 <= hora < 24:
    print("é noite")


