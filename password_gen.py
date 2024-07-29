import random
import string
import hashlib

# Função para gerar uma senha aleatória
def gerar_senha(tamanho=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Função para criptografar uma senha
def criptografar_senha(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

# Função principal
def menu():
    senhas = {}
    while True:
        print("\nMenu:")
        print("1 - Criar uma nova senha")
        print("2 - Atualizar uma senha existente")
        print("3 - Apagar uma senha do sistema")
        print("4 - Criptografar a senha atual")
        print("5 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            nome = input("Digite um nome para a senha: ")
            senha = gerar_senha()
            senhas[nome] = senha
            print(f"Senha criada para {nome}: {senha}")

        elif opcao == '2':
            nome = input("Digite o nome da senha a ser atualizada: ")
            if nome in senhas:
                senha = gerar_senha()
                senhas[nome] = senha
                print(f"Senha atualizada para {nome}: {senha}")
            else:
                print("Senha não encontrada.")

        elif opcao == '3':
            nome = input("Digite o nome da senha a ser apagada: ")
            if nome in senhas:
                del senhas[nome]
                print(f"Senha para {nome} apagada.")
            else:
                print("Senha não encontrada.")

        elif opcao == '4':
            nome = input("Digite o nome da senha a ser criptografada: ")
            if nome in senhas:
                senha_criptografada = criptografar_senha(senhas[nome])
                senhas[nome] = senha_criptografada
                print(f"Senha criptografada para {nome}: {senha_criptografada}")
            else:
                print("Senha não encontrada.")

        elif opcao == '5':
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
     menu()
