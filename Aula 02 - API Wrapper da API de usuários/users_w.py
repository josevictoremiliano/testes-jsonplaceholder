import requests
global api_url
api_url = "https://jsonplaceholder.typicode.com/users/"

class users:
    def __init__(self):
        pass

    
    def Create_User(self, name, username, email):
        return requests.post(api_url, data = {"name": name, "username": username, "email": email}).status_code

    
    def Update_User(self, id, name, username, email):
        return requests.put(api_url + id, data={"name": name, "username": username, "email": email})

    def Delete_User(self):
        id = input("Digite o id do usuário: ")
        response = requests.get(api_url + id)
        if response.status_code == 200:
            requests.delete(api_url + id)
            print("Usuário deletado com sucesso")
            print( response.status_code)
        else:
            print("Usuário não encontrado")
        

    def List_User(self):
        response = requests.get(api_url)
        if response.status_code == 200:
            usuarios = response.json()
            for usuario in usuarios:
                print(usuario["id"], usuario["name"])
        return 0