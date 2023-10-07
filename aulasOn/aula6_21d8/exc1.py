#busca binaria
lista =[3,6,9,12,15,18,21,24]
valor_procurado = 20
encontrado = None
inicio = 0
termino = len(lista) - 1
meio = int(((termino - inicio)/2)+inicio)

if valor_procurado == lista[meio]:
    encontrado = meio
elif valor_procurado > lista[meio]:
    if termino == meio:
        pass
    else:
        inicio = meio + 1
elif valor_procurado < lista[meio]:
    if inicio == meio:
        pass
    else:
        termino = meio - 1


print("Valor encontrado em: ", encontrado)