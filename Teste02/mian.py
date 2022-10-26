from users_w import users as users

class execute:
    def __init__(self,):
        self.menu()

    def menu(self):
        print('''
        0 - Criar usuário
        1 - Atualizar usuário
        2 - Deletar usuário
        3 - Listar usuário
        4 - Sair
        ''')
    
        while True:
            opcao = input("Digite a opção desejada: ")
            if opcao == "0":
                name = input('Digite o nome do usuário: ')
                username = input('Qual username: ')
                email = input('Agora digite o email: ')
                print('Usuário criado! ', users.create_user(self, name, username, email))
            elif opcao == "1":
                users.Update_User(self)
            elif opcao == "2":
                users.Delete_User(self)
            elif opcao == "3":
                users.List_User(self)
            elif opcao == "4":
                exit()
            else:
                print("Opção inválida")
                print()
                self.menu()

if __name__ == "__main__":
    crud = execute()