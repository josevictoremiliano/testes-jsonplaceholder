from urllib import response
import requests
global api_url
global api_url_todos
api_url = "https://jsonplaceholder.typicode.com/users/"

class users:
    def __init__(self):
        pass

    
    def Create_User(self, name, username, email):
        print("Inserir usuário")
        name = input("Digite o nome do usuário: ")
        username = input("Digite o nome de usuário: ")
        email = input("Digite o email do usuário: ")
            
        response = requests.post(api_url, data = {"name": name, "username": username, "email": email})

        return 
    
    def Update_User(self, id, name, username, email):
        return requests.put(api_url + id, data={"name": name, "username": username, "email": email})

    def Delete_User(self):
        id = input("Digite o id do usuário: ")
        response = requests.get(api_url + id)
        if response.status_code == 200:
            requests.delete(api_url + id)
            print("Usuário deletado com sucesso")
        else:
            print("Usuário não encontrado")
        

    def List_User(self):
        response = requests.get(api_url)
        if response.status_code == 200:
            usuarios = response.json()
            for usuario in usuarios:
                print(usuario["id"], usuario["name"])
        return 0