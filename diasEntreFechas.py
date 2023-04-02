from datetime import date


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

    today = date(date.today().year, 
                  date.today().month, 
                  date.today().day)

    day   = int(input("Dia final: "))
    month = int(input("Mes final: "))
    year  = int(input("Año final: "))

    desired_date = date(year, month, day)
    
    delta = desired_date - today

    print(f"\nFaltan {delta.days} dias para la fecha!\n")

while True:
    print("Bienvenido")
    print("¿Que opción deseas?")
    print("Dias entre fechas ---- 1")
    print("Dias para ------------ 2")
    print("Salir ---------------- 3")

    op = int(input("Opcion: "))
    if op == 1:
        diasEntreFechas()
    elif op == 2:
        diasPara()
    else:
        exit()

