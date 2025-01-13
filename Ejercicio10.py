def determinar_dia_semana(numero):
    # Lista de nombres de días de la semana
    dias_semana = ['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo']
    
    # Verificar si el número está dentro del rango válido
    if numero >= 1 and numero <= 7:
        return dias_semana[numero - 1]
    else:
        return "Número inválido. Debe ser un número del 1 al 7."

# Solicitar al usuario que ingrese un número para determinar el día de la semana
try:
    num_dia = int(input("Ingrese un número del 1 al 7 para determinar el día de la semana: "))
    
    # Llamar a la función para determinar el día de la semana
    dia_semana = determinar_dia_semana(num_dia)
    
    # Mostrar el resultado
    print(f"El día correspondiente al número {num_dia} es: {dia_semana}")
except ValueError:
    print("Error: Ingrese un valor numérico.")
    