# Función para determinar si es mayor de edad
def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

# Solicitar al usuario que ingrese su edad
try:
    edad = int(input("Ingrese su edad: "))

    # Verificar si es mayor de edad usando la función
    if es_mayor_de_edad(edad):
        print("Eres mayor de edad.")
    else:
        print("Eres menor de edad.")
except ValueError:
    print("Error: Ingrese un valor numérico para la edad.")

    