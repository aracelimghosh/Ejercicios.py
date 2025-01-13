# Solicitar al usuario que ingrese una oración
oracion = input("Ingresa una oración: ")

# Dividir la oración en palabras
palabras = oracion.split()

# Contar la cantidad de palabras
cantidad_palabras = len(palabras)

# Mostrar el resultado al usuario
print(f"La oración contiene {cantidad_palabras} palabras.")
