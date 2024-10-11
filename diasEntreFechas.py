from datetime import date, timedelta

def diasEntreFechas():
    f_day   = int(input("Dia inicial: "))
    f_month = int(input("Mes inicial: "))
    f_year  = int(input("Año inicial: \n"))
    first_date = date(f_year, f_month, f_day)

    l_day   = int(input("Dia final: "))
    l_month = int(input("Mes final: "))
    l_year  = int(input("Año final: "))
    last_date = date(l_year, l_month, l_day)
    delta = last_date - first_date

    print(f"\nHay {delta.days} dias entre las 2 fechas\n")


def diasPara():
    today = date.today()

    day   = int(input("Dia final: "))
    month = int(input("Mes final: "))
    year  = int(input("Año final: "))

    desired_date = date(year, month, day)
    
    delta = desired_date - today

    print(f"\nFaltan {delta.days} dias para la fecha!\n")


def sumarDiasDesdeHoy():
    today = date.today()
    dias = int(input("¿Cuántos días deseas sumar a la fecha de hoy?: "))

    nueva_fecha = today + timedelta(days=dias)

    print(f"\nLa fecha después de {dias} días será: {nueva_fecha.strftime('%d/%m/%Y')}\n")


while True:
    print("Bienvenido")
    print("¿Qué opción deseas?")
    print("1. Días entre fechas")
    print("2. Días para una fecha")
    print("3. Sumar días a partir de hoy")
    print("4. Salir")

    op = int(input("Opción: "))
    if op == 1:
        diasEntreFechas()
    elif op == 2:
        diasPara()
    elif op == 3:
        sumarDiasDesdeHoy()
    else:
        exit()
