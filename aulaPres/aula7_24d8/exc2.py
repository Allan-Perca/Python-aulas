caminho = "./notas.txt"
arquivo = open(caminho, "r")

linha = None

while linha != "":
    linha = arquivo.readline()
    lista = linha.split(",")
    soma = int(lista[1]) + int(lista[2]) + int(lista[3]) + int(lista[4])
    print("nome: ", lista[0], "soma: ", soma)

while linha != "":
    linha = arquivo.readline()
    lista = linha.split(",")
    for lista in range(1, len(lista)):
        i = 0
        num = int(lista[i])
        i = i + 1
    
        

