def dividir(numero, divisor):
    return numero / divisor

try:
    numero = float(input("Digite um valor: "))
    divisor = float(input("Digite o divisor: "))
    print(f"A divisão de {numero:.2f} por {divisor:.2f} é: {dividir(numero, divisor):.2f}")

except ZeroDivisionError:
    print("Divisor inválido. Não existe divisão por 0.")