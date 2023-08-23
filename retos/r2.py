def calcular_costo_estacionamiento(dia_semana, tiempo_estacionado):
    tarifa = 0
    
    if dia_semana.lower() == "lunes" or dia_semana.lower() == "martes" or dia_semana.lower() == "miércoles":
        tarifa = 2.00
    elif dia_semana.lower() == "jueves" or dia_semana.lower() == "viernes":
        tarifa = 2.50
    elif dia_semana.lower() == "sábado" or dia_semana.lower() == "domingo":
        tarifa = 3.00
    else:
        print("Día de la semana incorrecto.")
        return

    horas = int(tiempo_estacionado)
    minutos = int((tiempo_estacionado - horas) * 60)

    if minutos > 0:
        horas += 1

    costo_total = tarifa * horas
    return costo_total

dia = input("Ingrese el día de la semana: ")
tiempo = float(input("Ingrese el tiempo estacionado (en horas): "))

costo = calcular_costo_estacionamiento(dia, tiempo)
if costo > 0:
    print(f"El costo de estacionamiento es: ${costo:.2f}")