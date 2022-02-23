from datetime import date


def diasEntreFechas():
    x = int(input("Dia inicial: "))
    y = int(input("Mes inicial: "))
    z = int(input("Año inicial: "))
    f_date = date(z, y, x)
    print()
    x1 = int(input("Dia final: "))
    y1 = int(input("Mes final: "))
    z1 = int(input("Año final: "))
    l_date = date(z1, y1, x1)
    delta = l_date - f_date

    print()
    print(f"Hay {delta.days} dias entre las 2 fechas")
    print()


def diasPara():
    x = date.today().day
    y = date.today().month
    z = date.today().year
    f_date = date(z, y, x)

    x1 = int(input("Dia final: "))
    y1 = int(input("Mes final: "))
    z1 = int(input("Año final: "))
    l_date = date(z1, y1, x1)
    delta = l_date - f_date

    print()
    print(f"Faltan {delta.days} dias para la fecha!")
    print()

while True:
    print("Bienvenido")
    print("¿Que opción deseas?")
    print("Dias entre fechas ---- 1")
    print("Dias para ------------ 2")
    print("Salir ---------------- 3")

    x = int(input("Opcion: "))
    if x == 1:
        diasEntreFechas()
    elif x == 2:
        diasPara()
    else:
        exit()

