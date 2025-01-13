# Solicitar al usuario un número
numero = int(input("Ingresa un número: "))

# Verificar si el número es primo
es_primo = True

if numero <= 1:
    es_primo = False
else:
    for i in range(2, int(numero**0.5) + 1):  # Revisar hasta la raíz cuadrada del número
        if numero % i == 0:
            es_primo = False
            break

# Mostrar el resultado
if es_primo:
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")

