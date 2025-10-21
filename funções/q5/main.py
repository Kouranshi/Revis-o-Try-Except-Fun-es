def calcular_imc(peso, altura):
    return (peso / (altura**2))

def classificar_imc(imc):
    if imc < 18.5:
        print("Abaixo do peso.")
    elif imc >= 18.5 and imc <= 24.9:
        print("Peso normal.")
    else:
        print("Acima do peso.")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

classificar_imc(calcular_imc(peso, altura))