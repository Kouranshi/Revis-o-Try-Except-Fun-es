def autenticacao (email, senha):
    if email == "admin" and senha == "admin":
        return True
    
email = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if autenticacao(email, senha) == True:
    print("Login com sucesso!")
else:
    print("Usuário ou senha incorreto.")