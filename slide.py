hora = float(input("Que horas sao? "))
if hora > 0 and hora < 6:
    print("Boa madrugada")
elif hora > 7 and hora < 12:
    print("Bom dia")
elif hora > 13 and hora < 18:
    print("Boa tarde")
elif hora > 19 and hora <= 24:
    print("Boa noite")