# Función para convertir dólares a euros
def dolares_a_euros(dolares):
    # Tipo de cambio actual (1 dólar = 0.85 euros)
    tipo_cambio = 0.85
    
    # Calcular la cantidad en euros
    euros = dolares * tipo_cambio
    return euros

# Solicitar al usuario que ingrese la cantidad en dólares
try:
    dolares = float(input("Ingrese la cantidad en dólares que desea convertir a euros: $"))
    
    # Llamar a la función para convertir dólares a euros
    cantidad_euros = dolares_a_euros(dolares)
    
    # Mostrar el resultado
    print(f"${dolares} dólares son {cantidad_euros:.2f} euros.")
except ValueError:
    print("Error: Ingrese un valor numérico para la cantidad en dólares.")