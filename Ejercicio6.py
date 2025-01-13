def es_palindromo(palabra):
    # Eliminar espacios en blanco y convertir a minúsculas
    palabra = palabra.replace(" ", "").lower()
    
    # Comparar la palabra con su reverso
    if palabra == palabra[::-1]:
        return True
    else:
        return False

# Solicitar al usuario que ingrese una palabra
palabra_usuario = input("Ingrese una palabra para verificar si es un palíndromo: ")

# Llamar a la función es_palindromo() y mostrar el resultado
if es_palindromo(palabra_usuario):
    print(f"La palabra '{palabra_usuario}' es un palíndromo.")
else:
    print(f"La palabra '{palabra_usuario}' no es un palíndromo.")
    