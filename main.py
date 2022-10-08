from defs import *

print("Bem vindo a API Json Placeholder")

#Menu
return_menu()

while True:
    opcao = input("Digite a opção desejada: ")
    if opcao == "1":
        print("Listar usuários")
        print()
        listar_usuarios()
        print()
        print("Fim da listagem")

    elif opcao == "2":
        print("Buscar usuário")
        buscar_usuario()
        print("Fim da listagem")
        
    elif opcao == "3":
        inserir_usuario()
        print("Usuário inserido com sucesso")
        return_menu()
    elif opcao == "4":
        
        alterar_usuario()
       
        return_menu()
    elif opcao == "5":
        deletar_usuario()

        return_menu()
    elif opcao == "6":
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
        return_menu()