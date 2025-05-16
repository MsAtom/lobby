import json
import os

# Funções para carregar e salvar usuários no arquivo
def carregar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as arquivo:
            dados = json.load(arquivo)
            # Corrige dados antigos (login: "senha")
            for login, info in dados.items():
                if isinstance(info, str):
                    dados[login] = {"senha": info, "curso": None}
            return dados
    return {}

def salvar_usuarios(usuarios):
    with open("usuarios.json", "w", encoding="utf-8") as arquivo:
        json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)

cursos_disponiveis = [
    {
        "nome": "Introdução à Língua Brasileira de Sinais (Libras)",
        "carga_horaria": "60h",
        "descricao": "Apresenta práticas de Libras para apoiar o uso como meio de comunicação e o atendimento adequado às pessoas com deficiência auditiva."
    },
    {
        "nome": "Introdução à Audiodescrição",
        "carga_horaria": "40h",
        "descricao": "Apresenta recursos de audiodescrição em sites, redes sociais e publicações para auxiliar a compreensão de pessoas com deficiência visual, com deficiência intelectual, com dislexia e pessoas idosas."
    },
    {
        "nome": "Acessibilidade na Comunicação",
        "carga_horaria": "30h",
        "descricao": "Apresenta o conceito biopsicossocial e terminologias relacionadas a pessoas com deficiência, legislação, acessibilidade, recursos e técnicas, e exemplos práticos de comunicação acessível em eventos presenciais, web e impressos."
    }
]

def criar_login():
    usuarios = carregar_usuarios()
    print("\n=== Criar Novo Login ===")
    login = input("Digite seu novo login: ")
    if login in usuarios:
        print("Login já existe. Tente outro.")
    else:
        senha = input("Digite sua nova senha: ")
        usuarios[login] = {
            "senha": senha,
            "curso": None
        }
        salvar_usuarios(usuarios)
        print("Conta criada com sucesso!")

def fazer_login():
    usuarios = carregar_usuarios()
    print("\n=== Login ===")
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")

    if login in usuarios and usuarios[login]["senha"] == senha:
        print(f"\nLogin bem-sucedido!")
        menu_cursos(login)
    else:
        print("Login ou senha incorretos.")

def menu_cursos(login):
    usuarios = carregar_usuarios()
    negrito = "\033[1m"
    reset = "\033[0m"

    while True:
        print("\n--- MENU DE CURSOS ---")
        print("1. Ver cursos disponíveis")
        print("2. Inscrever-se em um curso")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print(f"\n{negrito}--- CURSOS DISPONÍVEIS ---{reset}\n")
            for i, curso in enumerate(cursos_disponiveis, 1):
                print(f"{negrito}Curso {i}:{reset}")
                print(f"{negrito}Nome:{reset} {curso['nome']}")
                print(f"{negrito}Carga horária:{reset} {curso['carga_horaria']}")
                print(f"{negrito}Descrição:{reset} {curso['descricao']}")
                print("-" * 60)
        elif opcao == "2":
            print("\nDigite o número do curso que deseja se inscrever:")
            for i, curso in enumerate(cursos_disponiveis, 1):
                print(f"{i}. {curso['nome']} ({curso['carga_horaria']})")
            try:
                escolha = int(input("Número do curso: "))
                if 1 <= escolha <= len(cursos_disponiveis):
                    curso_escolhido = cursos_disponiveis[escolha - 1]["nome"]
                    usuarios[login]["curso"] = curso_escolhido
                    salvar_usuarios(usuarios)
                    print(f"{negrito}Inscrição realizada no curso: {curso_escolhido}{reset}")
                else:
                    print("Curso inválido.")
            except ValueError:
                print("Digite um número válido.")
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
