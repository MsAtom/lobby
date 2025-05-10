usuarios = {}  # Dicionário para armazenar usuários e senhas
cursos_disponiveis = ["Python Básico", "Tecnologia Assistiva", "Acessibilidade Digital", "Introdução à Programação"]

def criar_login():
    print("\n=== Criar Novo Login ===")
    login = input("Digite seu novo login: ")
    if login in usuarios:
        print("Login já existe. Tente outro.")
    else:
        senha = input("Digite sua nova senha: ")
        usuarios[login] = senha
        print("Conta criada com sucesso!")

def fazer_login():
    print("\n=== Login ===")
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    if login in usuarios and usuarios[login] == senha:
        print(f"Bem-vindo, {login}!")
        menu_cursos()
    else:
        print("Login ou senha incorretos.")

def menu_cursos():
    while True:
        print("\n--- MENU DE CURSOS ---")
        print("1. Ver cursos disponíveis")
        print("2. Inscrever-se em um curso")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("\nCursos disponíveis:")
            for i, curso in enumerate(cursos_disponiveis, 1):
                print(f"{i}. {curso}")
        elif opcao == "2":
            print("\nDigite o número do curso que deseja se inscrever:")
            for i, curso in enumerate(cursos_disponiveis, 1):
                print(f"{i}. {curso}")
            escolha = int(input("Número do curso: "))
            if 1 <= escolha <= len(cursos_disponiveis):
                print(f"Inscrição realizada no curso: {cursos_disponiveis[escolha - 1]}")
            else:
                print("Curso inválido.")
        elif opcao == "3":
            print("Saindo do menu de cursos.")
            break
        else:
            print("Opção inválida.")

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Fazer login")
        print("2. Criar novo login")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            fazer_login()
        elif escolha == "2":
            criar_login()
        elif escolha == "3":
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida.")

# Início do programa
menu_principal()