import requests
global api_url
global api_url_todos
api_url = "https://jsonplaceholder.typicode.com/users"

class User:
    def __init__(self, id, name, username, email):
        self.id = id
        self.name = name
        self.username = username
        self.email = email

    def __str__(self):
        return f"User: {self.name}, {self.username}, {self.email}"
    
    def Create_User(self, name, username, email):
        response = requests.post(api_url, data={"name": name, "username": username, "email": email})
        return 0
    
    def Update_User(self, id, name, username, email):
        response = requests.get(api_url + id)
        if response.status_code == 200:
            user = response.json()
            print("Usuario com o nome: [", user["name"], "] encontrado")
            print("username: ", user["username"] + ", email: ", user["email"])
            print()
            print("Digite os novos dados do usuário")
            name = input("Digite o nome do usuário: ")
            username = input("Digite o username de usuário: ")
            email = input("Digite o email do usuário: ")
            response = requests.put(api_url + id, data={"name": name, "username": username, "email": email})
            print()
            print(response.status_code)
            print()
        return 0

    def Delete_User(self, id):
        response = requests.get(api_url + id)
        if response.status_code == 200:
            user = response.json()
            print("Usuario com o nome: [", user["name"], "] encontrado")
            print("username: ", user["username"] + ", email: ", user["email"])
            print()
            print("Deseja realmente deletar o usuário?")
            opcao = input("Digite 1 para sim e 2 para não: ")
            if opcao == "1":
                response = requests.delete(api_url + id)
                print()
                print(response.status_code)
                print()
            elif opcao == "2":
                print("Usuário não deletado")
                print()
        return 0

    def List_User(self, id, name, username, email):
        response = requests.get(api_url + id)
        if response.status_code == 200:
            user = response.json()
            print("Usuario com o nome: [", user["name"], "] encontrado")
            print("username: ", user["username"] + ", email: ", user["email"])
            print()
        return 0