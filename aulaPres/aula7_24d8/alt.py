def troca_simples(letra):
    if letra.lower() == "o":
        letra = 0
    elif letra.lower() == "a":
        letra = 4
    elif letra.lower() == "t":
        letra = 7
    elif letra.lower() == "i":
        letra = 1
    elif letra.lower() == "e":
        letra = 3
    return letra

def troca_facil(letra):
    lista = ["a", "e", "i", "o", "t"]
    lista_troca = ["4", "3", "1", "0", "7"]
    indice = 0
    for item in lista:
        if item == letra:
            return lista_troca[indice]
        indice = indice + 1
    return letra

def troca_dicionario( letra ): 
    lista_troca = {"a": "4", "e": "3", "i": "1", "o": "0", "t": "7"} 
    if letra in lista_troca:
        return lista_troca[letra]
    else:
        return letra

    # try:
    #     indice = lista.index(letra)
    #     if indice >= 0:
    #         return lista_troca[indice]
    # except:
    #     return letra  
    
caminho_arquivo = "C:\\Users\\logonrmlocal\\Downloads\\New folder\\hello.txt"
arquivo = open(caminho_arquivo, "r")
letra = None
while letra != "":
    i = 1
    letra = arquivo.read(i)
    i = i + 1
    
    print(troca_facil(letra))