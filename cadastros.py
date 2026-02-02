pessoas = []
opcao = 0
caminho = "/Users/Yago/OneDrive/Área de Trabalho/Cadastro de Cliente/lista.txt"
dados = open(caminho, "r") #"r" siginifica que abri o arquivo no modo "read" (ou seja, leitura)

#dados = open("lista.txt", "w") // usa o "w" para o modo "write" (ou seja, escrever)
#dadosSalvos = dados.write("Aqui eu adiciono algo no aquivo")

dadosSalvos = dados.read()
dados.close()

print(f" Os dados já salvos são: \n {dadosSalvos}")

print("")
print("------- MENU -------")    
print("Opção 1 - Cadastrar nova pessoa")
print("Opção 2 - Listar as pessoas")
print("Opção 3 - Sair")

def cadastrarPessoa():
    pessoas.append(input("Nome da pessoa: "))
    
    with open(caminho, "a") as arquivo: # o "a" significa adicionar
        arquivo.write(f"{pessoas[-1]} \n")

def listarPessoas():
    with open(caminho, "r") as arquivo: 
        dadosSalvos = arquivo.read()
    print(dadosSalvos)

while opcao != 3:
    opcao = int(input("Digite a opção digitada: "))
    if opcao == 1:
        cadastrarPessoa()
    elif opcao == 2:
        listarPessoas() 
    elif opcao == 3:
        break    
    else:
        print("Opção inválida, tente novamente")   

print("Loop finalizado")
