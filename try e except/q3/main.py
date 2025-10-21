try:
    def divisao(numero, divisor):
        return numero / divisor
    
    numero = float(input("Digite um valor: "))
    divisor = float(input("Digite o divisor: "))
    print(f"A divisão de {numero:.2f} por {divisor:.2f} é: {divisao(numero, divisor):.2f}")

except ZeroDivisionError:
    print("Não existe divisão por 0.")

except ValueError:
    print("Valor inválido. Por favor, digite apenas números.")