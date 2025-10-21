def desconto (valor):
    desconto = valor - (valor * 0.1)
    return desconto

valor = float(input("Digite o valor do produto: "))

print(f"O valor do produto com desconto de 10% é: {desconto(valor):.2f}")