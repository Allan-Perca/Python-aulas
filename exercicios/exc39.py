# Faça um código para ler as linhas do arquivo a.csv, adicionar 1,0 ponto na nota de cada aluno e gravar o conteúdo no arquivo b.csv contendo o mesmo nome e a nova nota. O arquivo a.csv possui os campos Nome e Nota separados por ( ; ) cada linha corresponde a um nome e uma nota.

# Exemplo do arquivo de origem a.csv:
# Antonio Rodrigues; 6,5
# Katia Toledo; 7,4
# Guilherme Prado; 4,6

# Exemplo de arquivo de destino b.csv:
# Antonio Rodrigues; 7,5
# Katia Toledo; 8,4
# Guilherme Prado; 5,6

arquivo_leitura = open("./a.csv", "r")
arquivo_destino = open("./b.csv", "w")

linha = None

while linha != "":
    linha = arquivo_leitura.readline()
    if linha != "":
        linha_lista = linha.split(";")
        #necesssario transformar a nota em float, e substituir a , do numero por . para calcular como numero e n strg
        nova_nota = float(linha_lista[1].replace(",", ".")) + 1.0
        nova_linha = "{}, {:,}\n".format(linha_lista[0], nova_nota)
        print("Nome: ", linha_lista[0])
        print("Nota: ", nova_nota)
        print("Nova linha:", nova_linha)
        arquivo_destino.write(nova_linha)

arquivo_leitura.close()
arquivo_destino.close()

