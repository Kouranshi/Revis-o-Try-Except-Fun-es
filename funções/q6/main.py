def imposto(preco):
    return preco + (preco * 0.15)

preco = float(input("Digite o preço do produto: "))
print(f"O valor do produto + 15% de imposto é: {imposto(preco)}")