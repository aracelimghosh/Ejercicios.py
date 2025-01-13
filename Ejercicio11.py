from datetime import date

# Obtener el año actual
año_actual = date.today().year

# Solicitar el año de nacimiento al usuario
año_nacimiento = int(input("Por favor, ingresa tu año de nacimiento: "))

# Calcular la edad
edad = año_actual - año_nacimiento

# Mostrar la edad al usuario
print(f"Tienes {edad} años.")
