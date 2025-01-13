# Solicitar al usuario una lista de números separados por comas
entrada = input("Ingresa una lista de números separados por comas: ")

# Convertir la entrada en una lista de números
numeros = [int(num) for num in entrada.split(",")]

# Inicializar contadores
pares = 0
impares = 0

# Contar pares e impares
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Mostrar los resultados
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
