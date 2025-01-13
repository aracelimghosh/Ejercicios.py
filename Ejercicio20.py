# Solicitar al usuario una lista de números separados por comas
entrada = input("Ingresa una lista de números separados por comas: ")

# Convertir la entrada en una lista de números
numeros = [float(num) for num in entrada.split(",")]

# Calcular la suma de todos los números
suma_total = sum(numeros)

# Mostrar el resultado al usuario
print(f"La suma de los números es: {suma_total}")
