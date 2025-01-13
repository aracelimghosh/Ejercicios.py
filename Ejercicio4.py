# Inicializar la variable para almacenar la suma
suma_pares = 0

# Iterar sobre los números del 1 al 100 (incluyendo 100)
for num in range(1, 101):
    # Verificar si el número es par
    if num % 2 == 0:
        # Sumar el número al acumulador suma_pares
        suma_pares += num

# Mostrar el resultado
print(f"La suma de todos los números pares del 1 al 100 es: {suma_pares}")
