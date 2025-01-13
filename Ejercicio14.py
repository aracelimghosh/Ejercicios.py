# Solicitar al usuario el precio original del artículo
precio_original = float(input("Ingresa el precio original del artículo: "))

# Calcular el descuento
descuento = precio_original * 0.20

# Calcular el precio final
precio_final = precio_original - descuento

# Mostrar el precio final al usuario
print(f"El precio final del artículo después del descuento es: ${precio_final:.2f}")
