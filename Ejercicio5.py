# Función para contar vocales en una palabra
def contar_vocales(palabra):
    # Convertir la palabra a minúsculas para simplificar la verificación
    palabra = palabra.lower()
    
    # Inicializar contador de vocales
    contador = 0
    
    # Definir conjunto de vocales
    vocales = {'a', 'e', 'i', 'o', 'u'}
    
    # Iterar sobre cada letra en la palabra
    for letra in palabra:
        # Verificar si la letra es una vocal
        if letra in vocales:
            contador += 1
    
    return contador

# Solicitar al usuario que ingrese una palabra
palabra_usuario = input("Ingrese una palabra para contar las vocales: ")

# Llamar a la función contar_vocales() y mostrar el resultado
num_vocales = contar_vocales(palabra_usuario)
print(f"La palabra '{palabra_usuario}' tiene {num_vocales} vocales.")
