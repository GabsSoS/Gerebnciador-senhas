import json
import os

ARQUIVO = "senha.json"

# Função para carregar dados existentes
def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Função para salvar dados
def salvar_dados(dados):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)

# Adicionar nova senha
def adicionar_senha():
    site = input("Site: ").strip()
    login = input("Login: ").strip()
    senha = input("Senha: ").strip()

    dados = carregar_dados()
    dados[site] = {"login": login, "senha": senha}
    salvar_dados(dados)
    print(f" Senha salva para o site: {site}")

# Mostrar todas as senhas
def mostrar_senhas():
    dados = carregar_dados()
    if not dados:
        print(" Nenhuma senha salva.")
        return
    for site, info in dados.items():
        print(f"\nSite: {site}")
        print(f" Login: {info['login']}")
        print(f" Senha: {info['senha']}")

# Buscar senha por site
def buscar_senha():
    site = input("Digite o site: ").strip()
    dados = carregar_dados()
    if site in dados:
        print(f"\n Login: {dados[site]['login']}")
        print(f" Senha: {dados[site]['senha']}")
    else:
        print(" Site não encontrado.")

# Menu principal
def menu():
    while True:
        print("\n=== GERENCIADOR DE SENHAS ===")
        print("1. Adicionar nova senha")
        print("2. Mostrar todas as senhas")
        print("3. Buscar senha por site")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_senha()
        elif opcao == "2":
            mostrar_senhas()
        elif opcao == "3":
            buscar_senha()
        elif opcao == "4":
            print("Saindo")
            break
        else:
            print("Opção inválida.")


menu()
