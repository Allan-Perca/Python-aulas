#crud no arquivo
alunos = []

def menu():
    escolha = None
    while escolha == None:
        print("Gestão de Alunos")
        print("(N)ovo Aluno")
        print("(L)istar Alunos")
        print("(E)ditar Aluno")
        print("(A)pagar Alunos")
        print("(G)ravar os dados")
        print("(S)air")
        opcao = input("Informe a opção escolhida: ").lower()
        if opcao in ['n', 'l', 'e', 'a', 's', 'g']:
            escolha = opcao
        else:
            print("...Opção invalida ... \n\n")
    return escolha

def novoAluno():
    print("Novo aluno")
    nome = input("Nome: ")
    ra = input("RA: ")
    alunos.append({"nome": nome, "ra": ra})

def listarAlunos():
    print("Lista de alunos")
    for aluno in alunos:
        print("{} - {}".format(aluno["ra"], aluno["nome"]))
    print("\n\n")

def editarAluno():
    print("Editar aluno")
    ra = input("Informe o RA do aluno")
    for aluno in alunos:
        if aluno["ra"] == ra:
            print("Aluno com RA {} encontrado".format(ra))
            print("Nome atual: {}".format(aluno["nome"]))
            aluno["nome"] = input("Informe o novo nome do aluno: ")

def gravarAlunos():
    arquivoAlunos = open("./exc3.csv", "w")
    for aluno in alunos:
        linha = "{}, {}\n".format(aluno["ra"], aluno["nome"])
        arquivoAlunos.write(linha)
    arquivoAlunos.close()

def lerAlunos():
    global alunos
    arquivoAlunos = open("./exc3.csv", "r")
    linha = None
    while linha != "":
        linha = arquivoAlunos.readline().strip() #strip remove da ponta da direita e da esquerda
        if linha != "":
            dadosAluno = linha.split(";")
            d = {"ra":dadosAluno[0], "nome":dadosAluno[1]}
            alunos.append(d)
    arquivoAlunos.close()


if __name__ == "__main__":
    while True:
        opcao = menu()
        #if opcao == "n": #match --> existe o match para se usar no lugar do if
        match opcao:
            case 'n':
                novoAluno()
            case 'l':
                listarAlunos()   
            case 'e':
                editarAluno()   
            case 'a':
                print("Apagar aluno") 
            case 'g':
                gravarAlunos()   
            case 's':
                print("Até mais")    
                break