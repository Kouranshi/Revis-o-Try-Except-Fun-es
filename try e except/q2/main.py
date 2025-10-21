try:
    numero = float(input("Digite um número: "))
    print(f"Seu número é: {numero:.2f}")

except ValueError:
    print("Valor inválido. Por favor, digite um número.")