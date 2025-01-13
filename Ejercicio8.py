def calcular_imc(peso, altura):
    # Calcular el IMC
    imc = peso / (altura ** 2)
    return imc

# Solicitar al usuario que ingrese su peso en kilogramos y altura en metros
try:
    peso = float(input("Ingrese su peso en kilogramos: "))
    altura = float(input("Ingrese su altura en metros: "))
    
    # Calcular el IMC llamando a la función
    imc = calcular_imc(peso, altura)
    
    # Mostrar el resultado
    print(f"Su Índice de Masa Corporal (IMC) es: {imc:.2f}")
except ValueError:
    print("Error: Ingrese valores numéricos para peso y altura.")
    