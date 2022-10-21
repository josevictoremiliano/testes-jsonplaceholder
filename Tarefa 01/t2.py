import defs as d

users = d.listar_usuarios()

print("Bem vindo a API Json Placeholder")

#Menu
d.return_menu()

while True:
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        print("Listar usuários")
        print()
        d.listar_usuarios(users)
        print()
        print("Fim da listagem")

    elif opcao == "2":
        print("Listar posts")
        print()
        d.listar_tarefas(users)
        print()
        print("Fim da listagem")
    elif opcao == "3":
        print("Buscar usuário")
        d.buscar_usuario(users)
        print("Fim da listagem")
    elif opcao == "4":
        d.inserir_usuario(users)
        print("Usuário inserido com sucesso")
        d.return_menu()
    elif opcao == "5":
        d.alterar_usuario(users)
        d.return_menu()
    elif opcao == "6":
        d.deletar_usuario(users)

        d.return_menu()
    elif opcao == "10":
        print()
        print("Sair do programa")
        print ("Obrigado por utilizar o programa")
        print()
        print()
        print()

        break
    else:
        print("~-~-~-~-~-~-~-~Opção inválida~-~-~-~-~-~-~-~")
        print("As opções são:")
        d.return_menu()
        print()

