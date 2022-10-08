#usando a https://jsonplaceholder.typicode.com/users/ listar usuarios, id e nome
import requests
api = "https://jsonplaceholder.typicode.com/users/"

def return_menu():
    print()
    print("1 - Listar usuários")
    print("2 - Buscar usuário")
    print("3 - Inserir usuário")
    print("4 - Alterar usuário")
    print("5 - Deletar usuário")
    print("6 - Sair do programa")
    print()
    return 0

def listar_usuarios():
    response = requests.get(api)

    #listar usuários somente o nome e id
    response = requests.get(api)
    if response.status_code == 200:
        usuarios = response.json()
        for usuario in usuarios:
            print(usuario["id"], usuario["name"])
            
    else:
        print("Erro na requisição, possivelmente o usuá1rio não existe")
    return 0

def buscar_usuario():
    id = input("Digite o id do usuário: ")
    response = requests.get(api + id)
    if response.status_code == 200:
        usuario = response.json()
        print()
        print("Nome: ", usuario["name"])
        print("Nome de usuário: ", usuario["username"])
        print("Email: ", usuario["email"])
        print("Endereço: ", usuario["address"]["street"] + ", " + usuario["address"]["suite"] + ", " + usuario["address"]["city"] + ", " + usuario["address"]["zipcode"])
        print()
    else:
        print("Erro na requisição, possivelmente o usuário não existe")
    return 0

def inserir_usuario():
    print("Inserir usuário")
    nome = input("Digite o nome do usuário: ")
    username = input("Digite o nome de usuário: ")
    email = input("Digite o email do usuário: ")
        
    response = requests.post(api, data = {"name": nome, "username": username, "email": email})

    return 0

def alterar_usuario():
    print("Alterar usuário")
    id = input("Digite o id do usuário: ")
    response = requests.get(api + id)
    if response.status_code == 200:
        
        user =response.json()
        print("Usuario com o nome: [", user["name"], "] encontrado")
        print("username: ", user["username"] + ", email: ", user["email"])
        print()
        print("Digite os novos dados do usuário")
        nome = input("Digite o nome do usuário: ")
        username = input("Digite o username de usuário: ")
        email = input("Digite o email do usuário: ")
        response = requests.put(api + id, data = {"name": nome, "username": username, "email": email})
        print()
        print(response.status_code)
        print()

    return 0

def deletar_usuario():
    print("Deletar usuário")
    id = input("Digite o id do usuário: ")
    response = requests.get(api + id)
    if response.status_code == 200:
        user =response.json()
        print("Usuario com o nome: [", user["name"], "] encontrado")
        print("username: ", user["username"] + ", email: ", user["email"])
        print()
        print("Deseja realmente deletar o usuário?")
        opcao = input("Digite 1 para sim e 2 para não: ")
        if opcao == "1":
            response = requests.delete(api + id)
            print()
            print(response.status_code)
            print()
        elif opcao == "2":
            print("Usuário não deletado")
            print()
        else:
            print("Opção inválida")
            print()
    else:
        print("Usuário não encontrado")
        print()
    return 0