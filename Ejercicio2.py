    
# Función para calcular el monto total con propina
def calcular_total_con_propina(total_cuenta):
    propina = total_cuenta * 0.15
    total_con_propina = total_cuenta + propina
    return total_con_propina

# Pedir al usuario que ingrese el total de la cuenta
total_cuenta = float(input("Ingrese el total de la cuenta en el restaurante: "))

# Calcular el total a pagar incluyendo la propina
total_a_pagar = calcular_total_con_propina(total_cuenta)

# Mostrar el resultado
print(f"El monto total a pagar, incluyendo una propina del 15%, es: {total_a_pagar:.2f}")