# Crie um arquivo texto chamado ola.txt e coloquem o arquivo em uma pasta de fácil acesso como c:\temp\ em seguida faça um programa que abra este arquivo e leia todo o conteúdo caractere a caractere mostrando-os em linhas separadas na tela (um caractere em cada linha)
# Modifique o programa anterior para trocar as letras por números antes de mostrar na tela conforme a tabela abaixo:
#              O - 0         S - 5
#              I - 1          G - 6
#              Z - 2         T - 7
#              E - 3         B - 8
#              A - 4
# Modifique o programa para gravar o conteúdo com as letras trocadas em outro arquivo chamado destino.txt

def troca_facil(letra):
    lista = ["a", "e", "i", "o", "t"]
    lista_troca = ["4", "3", "1", "0", "7"]
    indice = 0
    for item in lista:
        if item == letra:
            return lista_troca[indice]
        indice = indice + 1
    return letra

caminho_arquivo = "C:\\Users\\aperc\\1TDSPM\\hello.txt"
arquivo = open(caminho_arquivo, "r")
letra = None
while letra != "":
    i = 1
    letra = arquivo.read(i)
    i = i + 1
    
    print(troca_facil(letra))