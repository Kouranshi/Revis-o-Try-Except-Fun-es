def maior_ou_menor_idade(idade):
    if idade >= 18:
        print("Maior de idade.")
    elif idade < 18 and idade >= 0:
        print("Menor de idade.")
    else:
        print("Idade inválida.")

idade = int(input("Digite sua idade: "))
maior_ou_menor_idade(idade)