# Función para realizar la suma de dos números
def suma(num1, num2):
    return num1 + num2

# Función para realizar la resta de dos números
def resta(num1, num2):
    return num1 - num2

# Función para realizar la multiplicación de dos números
def multiplicacion(num1, num2):
    return num1 * num2

# Función para realizar la división de dos números
def division(num1, num2):
    # Manejar la división entre cero
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: No se puede dividir entre cero."

# Función principal para manejar la entrada del usuario y operaciones
def main():
    print("Operaciones disponibles:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    # Solicitar al usuario que elija una operación
    opcion = input("Ingrese el número de la operación que desea realizar (1/2/3/4): ")

    # Validar la opción ingresada
    if opcion in ['1', '2', '3', '4']:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))

        if opcion == '1':
            resultado = suma(num1, num2)
            operacion = "suma"
        elif opcion == '2':
            resultado = resta(num1, num2)
            operacion = "resta"
        elif opcion == '3':
            resultado = multiplicacion(num1, num2)
            operacion = "multiplicación"
        elif opcion == '4':
            resultado = division(num1, num2)
            operacion = "división"

        # Imprimir el resultado de la operación
        print(f"El resultado de la {operacion} es: {resultado}")
    else:
        print("Opción no válida. Por favor, ingrese un número válido (1/2/3/4).")

# Llamar a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
    

