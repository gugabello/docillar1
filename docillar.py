import hashlib
import json
import sys

#Login e Cadastro
def cadastrar_usuario(email, senha):
    # Hash da senha usando SHA-256
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    # Verifica se o email já está cadastrado
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['email'] == email:
            print("Este email já está cadastrado. Tente fazer login.")
            return False

    # Adiciona novo usuário ao JSON
    novo_usuario = {'email': email, 'senha_hash': senha_hash}
    usuarios.append(novo_usuario)
    salvar_usuarios(usuarios)
    
    print("Usuário cadastrado com sucesso!")
    return True

def fazer_login(email, senha):
    # Hash da senha usando SHA-256
    senha_hash = hashlib.sha256(senha.encode()).hexdigest()

    # Verifica se o email e a senha correspondem a um usuário cadastrado
    usuarios = carregar_usuarios()
    for usuario in usuarios:
        if usuario['email'] == email and usuario['senha_hash'] == senha_hash:
            print("Login bem-sucedido!")
            return True

    print("Login ou senha incorretos. Tente novamente.")
    return False

def carregar_usuarios():
    try:
        with open("usuarios.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Erro ao carregar o arquivo JSON. O conteúdo pode estar corrompido.")
        return []

def salvar_usuarios(usuarios):
    with open("usuarios.json", 'w') as file:
        json.dump(usuarios, file)


while True:
    print("-------Tela de Login-------\n\n")
    print("1. Cadastrar usuário")
    print("2. Fazer login")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        cadastrar_usuario(email, senha)
    elif opcao == "2":
        email = input("Digite seu email: ")
        senha = input("Digite sua senha: ")
        fazer_login(email, senha)
        break
    elif opcao == "0":
        print("Saindo do programa. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.\n")

#Pefil de usuario
def perfil_usuario():
    print("-------Perfil de Usuário-------\n\n")
    nome = input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    idade = input("Digite sua idade: ")
    endereco = input("Digite seu endereço: ")
    biografia = input("Digite sua biografia: ")
    ong = input("Você pertence a uma ONG? (S/N): ")

    # Salvar informações do usuário em um arquivo JSON
    usuario = {
        'nome': nome,
        'email': email,
        'idade': idade,
        'endereco': endereco,
        'biografia': biografia,
        'ong': ong
    }

    with open("perfil_usuario.json", 'w') as file:
        json.dump(usuario, file)

    print("Informações do perfil cadastradas com sucesso!")

def mostrar_perfil():
    try:
        with open("perfil_usuario.json", 'r') as file:
            usuario = json.load(file)
            print("\nPerfil do Usuário")
            print(f"Nome: {usuario['nome']}")
            print(f"E-mail: {usuario['email']}")
            print(f"Idade: {usuario['idade']}")
            print(f"Endereço: {usuario['endereco']}")
            print(f"Biografia: {usuario['biografia']}")
            print(f"ONG [S/N]: {usuario['ong']}\n")
    except FileNotFoundError:
        print("Perfil não encontrado. Cadastre suas informações primeiro.")


# MENU
def exibir_menu():
    print("1. Catálogo de pets")
    print("2. Carteira de vacina")
    print("3. Localização de ONGS")
    print("4. Perfil de usuário")
    print("5. Sair")

    #CATÁLOGO DE PETS

def main():
    while True:
        print("-------Menu Principal-------\n\n")
        exibir_menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            catalogo_animais()
        elif opcao == "2":
            carteira_vacina()
        elif opcao == "3":
            local_ongs()
        elif opcao =="4":
        
            while True:
                print("1. Cadastrar ou atualizar perfil de usuário")
                print("2. Mostrar perfil de usuário")
                print("0. Voltar para o menu")

                opcao = input("Escolha uma opção: ")

                if opcao == "1":
                    perfil_usuario()
                elif opcao == "2":
                    mostrar_perfil()
                elif opcao == "0":
                    break
                else:
                    print("Opção inválida. Tente novamente.\n")
        elif opcao == "5":
            sys.exit()
        else:
            print("Opção inválida. Escolha novamente.")

#catalogo de pets
def catalogo_animais():
    print("-------Catálogo de Pets-------\n\n")
    catalog = []

    def carregar_catalogo():
        try:
            with open("catalogo_animais.json", 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            print("Erro ao carregar o arquivo JSON. O conteúdo pode estar corrompido.")
            return []

    def salvar_catalogo(catalog):
        with open("catalogo_animais.json", 'w') as file:
            json.dump(catalog, file)

    def adicionar_animal(nome, especie, idade, sexo, descricao):
        animal = {
            'nome': nome,
            'especie': especie,
            'idade': idade,
            'sexo': sexo,
            'descricao': descricao
        }
        catalog.append(animal)
        salvar_catalogo(catalog)
        print("Animal adicionado com sucesso.")

    def listar_animais():
        if not catalog:
            print("O catálogo de animais está vazio.")
        else:
            for i, animal in enumerate(catalog, start=1):
                print(f"Animal {i}:")
                print(f"Nome: {animal['nome']}")
                print(f"Espécie: {animal['especie']}")
                print(f"Idade: {animal['idade']} anos")
                print(f"Sexo: {animal['sexo']}")
                print(f"Descrição: {animal['descricao']}\n")

    def adotar_animal(indice):
        if 1 <= indice <= len(catalog):
            adotado = catalog.pop(indice - 1)
            salvar_catalogo(catalog)
            print(f"Parabéns! Você adotou o animal {indice}.")
        else:
            print("Índice inválido.")

    # Main
    catalog = carregar_catalogo()

    while True:
        print("1. Adicionar animal")
        print("2. Adotar animal")
        print("3. Atualizar animal")
        print("4. Excluir animal")
        print("0. Voltar para o menu")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome: ")
            especie = input("Espécie: ")
            idade = input("Idade: ")
            sexo = input("Sexo: ")
            descricao = input("Descrição: ")
            adicionar_animal(nome, especie, idade, sexo, descricao)
        elif opcao == "2":
            listar_animais()
            indice = int(input("Digite o índice do animal a ser adotado: "))
            adotar_animal(indice)
        elif opcao == "3":
            listar_animais()
            indice = int(input("Digite o índice do animal a ser atualizado: "))
            nome = input("Nome: ")
            especie = input("Espécie: ")
            idade = input("Idade: ")
            sexo = input("Sexo: ")
            descricao = input("Descrição: ")
            atualizar_animal(indice, nome, especie, idade, sexo, descricao)
        elif opcao == "4":
            listar_animais()
            indice = int(input("Digite o índice do animal a ser removido: "))
            excluir_animal(indice)
        elif opcao == "0":
            main()
        else:
            print("Opção inválida. Tente novamente.")


    #CARTEIRA DE VACINA
#carteira de vacina
def carteira_vacina():
    print("-------Carteira de Vacina-------\n\n")
    registro_vacinas = []

    def adicionar_vacina():
        nome_pet = input("Nome do pet: ")
        nome_vacina = input("Nome da vacina: ")
        data_dose = input("Data da dose: (DD/MM/AAAA)")

        vacina = {
        "Nome do Pet": nome_pet,
        "Nome da Vacina": nome_vacina,
        "Data da Dose": data_dose
    }
        
        registro_vacinas.append(vacina)
        print("Informações da vacina registrada com sucesso!")

    def listar_vacinas():
        for vacina in registro_vacinas:
            print(vacina)
    
    while True:

        print("1. Adicionar informações de vacina")
        print("2. Listar informações de vacina")
        print("0. Voltar para o menu")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionar_vacina()
        elif opcao =="2":
            listar_vacinas()
        elif opcao == "0":
            main()
        else:
            print("Opção inválida. Escolha novamente.")


    #LOCALIZAÇÃO DE ONGS
def local_ongs():

    print("-------Localização das ONGS-------\n\n")
    adota_um_felino = ["Contato: (81) 97908-4149", "Localização: Casa Forte, Recife"]
    lar_bola_de_pelos = ["Contato: (81) 99990.3645", "Localização: Candeias, Jaboatão dos Guararapes"]
    abrigo_amo_animais = ["Contato: (81) 984748533", "Localização: Prado, Recife"]

    while True:
        print("1. Adota um Felino")
        print("2. Lar Bola de Pêlos")
        print("3. Abrigo Amo Animais")
        print("0. Voltar para o menu")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print (adota_um_felino)
            print ("1. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                local_ongs()
        elif opcao == "2":
            print(lar_bola_de_pelos)
            print ("1. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                local_ongs()
        elif opcao == "3":
            print(abrigo_amo_animais)
            print ("1. Voltar")
            opcao = input("Escolha uma opção: ")
            if opcao == "1":
                local_ongs()
        elif opcao == "0":
            main()
        else:
            print("Opção inválida. Escolha novamente.")

if __name__ == "__main__":
    main()