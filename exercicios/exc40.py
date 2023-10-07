# Crie um programa que leia os dados de um arquivo chamado notas.csv, transforme estes dados conforme abaixo e grave os em outro arquivo chamado notas_calculadas.csv

# Ler as linhas do arquivo notas.csv e mostrá-las na tela individualmente
# Mostrar apenas os nomes dos alunos
# Mostrar os nomes, a soma e a media das notas de cada aluno
# Mostrar a média geral da 1ª, 2ª, 3ª e 4ª notas, assim como a média geral de todas as notas
# Grave cada linha do aluno no outro arquivo notas_calculadas.csv contendo o nome, a nota 1, nota 2, nota 3, nota 4, soma das notas, e média do aluno

# Exemplo do arquivo de origem notas.csv:
#     João, 8.0, 6.5, 5.4, 7.2
#     Maria, 9.4, 7.2, 7.6, 8.1
#     Alberto, 6.4, 8.2, 7.1, 7.2
#     Junior, 5.3, 8.9, 4.6, 6.5

# Exemplo de arquivo de destino notas_calculadas.csv:
#     João, 8.0, 6.5, 5.4, 7.2, 27.1, 6.78 
#     Maria, 9.4, 7.2, 7.6, 8.1, 32.3, 8,1
#     Alberto, 6.4, 8.2, 7.1, 7.2, 28.9, 7,2
#     Junior, 5.3, 8.9, 4.6, 6.5, 25.3, 6.3

arquivo_origem = open("./notas.csv", "r")
arquivo_destino = open("notas_calculadas.csv", "w")

linha = None

while linha != "":
    linha = arquivo_origem.readline()
    if linha != "":
        lista = linha.split(",")
        linha_destino = "{}, ".format(lista[0])
        soma = 0
        for indice in range(1, 5): #for item in lista[1:]: --> pega os items a partir do indice 1
            item = float(lista[indice])
            soma = soma  + item #soma += item # 
            linha_destino = linha_destino + "{:4.1f}, ".format(item)
        media = soma / 4
        linha_destino = linha_destino + "{:5.2f}, {:5.1f}\n".format(soma, media)
        arquivo_destino.write(linha_destino)
        print(linha_destino)
        
        
        
        # print("Soma: {:5.2f}".format(soma))
        # print("Media: {:5.1f}".format(media))