opcao = 0
caminho = "/Users/Yago/OneDrive/Área de Trabalho/Cadastro de Cliente/lista.txt"
dados = open(caminho, "r") #"r" siginifica que abri o arquivo no modo "read" (ou seja, leitura)

#dados = open("lista.txt", "w") // usa o "w" para o modo "write" (ou seja, escrever)
#dadosSalvos = dados.write("Aqui eu adiciono algo no aquivo")

#dadosSalvos = dados.read()
#dados.close()

#print(f" Os dados já salvos são: \n {dadosSalvos}")

print("")
print("------- MENU -------")    
print("Opção 1 - Cadastrar nova pessoa")
print("Opção 2 - Listar as pessoas")
print("Opção 3 - Buscar pessoas")
print("Opção 4 - Remover pessoa")
print("Opção 5 - Sair")

def cadastrarPessoa():
    novo_usuario = input("Nome da pessoa: ")
    
    with open(caminho, "a") as arquivo: # o "a" significa adicionar
        arquivo.write(f"{novo_usuario} \n")

def listarPessoas():
    with open(caminho, "r") as arquivo: 
        dadosSalvos = arquivo.read()
    print(dadosSalvos)

def buscarPessoas():
    pessoa = input("Digite o nome da pessoa: ").strip().lower()

    with open(caminho, "r") as arquivo:
        linhas = [linha.strip().lower() for linha in arquivo]

    if pessoa in linhas:
        print(f"Usuário {pessoa} existente")
    else:
        print(f"Usuário {pessoa} inexistente")


def excluirPessoa():
    pessoa = input("Digite o nome da pessoa: ").strip().lower()

    with open(caminho, "r") as arquivo:
        linhas = arquivo.readlines()

    linhas = [linha.strip() for linha in linhas]

    if pessoa not in linhas:
        print(f"Usuário {pessoa} inexistente")
        return

    linhas.remove(pessoa)

    with open(caminho, "w") as arquivo:
        for nome in linhas:
            arquivo.write(nome + "\n")

    print(f"Usuário {pessoa} removido com sucesso!")

    
while opcao != 5:
    opcao = int(input("Digite a opção digitada: "))
    if opcao == 1:
        cadastrarPessoa()
    elif opcao == 2:
        listarPessoas() 
    elif opcao == 3:
        buscarPessoas()
    elif opcao == 4:
        excluirPessoa()
    elif opcao == 5:
        break    
    else:
        print("Opção inválida, tente novamente")   

print("Loop finalizado")
