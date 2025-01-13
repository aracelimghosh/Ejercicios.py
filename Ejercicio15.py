# Solicitar al usuario el número de minutos
minutos_totales = int(input("Ingresa la cantidad de minutos: "))

# Calcular las horas y los minutos restantes
horas = minutos_totales // 60
minutos_restantes = minutos_totales % 60

# Mostrar el resultado al usuario
print(f"{minutos_totales} minutos son {horas} horas y {minutos_restantes} minutos.")
