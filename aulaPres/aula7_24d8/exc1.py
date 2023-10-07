caminho_arquivo = "C:\\Users\\logonrmlocal\\Downloads\\New folder\\hello.txt"
arquivo = open(caminho_arquivo, "r")
#arquivo2 = open("./hello.txt", "r")
letra = None
while letra != "":
    i = 1
    letra = arquivo.read(i)
    i = i + 1
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
    print(letra)