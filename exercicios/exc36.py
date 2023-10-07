# Faça um programa para implementar o algoritmo Bubble Sort ensinado em aula. Conforme o fluxograma em anexo

lista = [7,15,8,2,22,4,1]

for j in range(0, len(lista)):
    for i in range(0, len(lista)-1):
        if lista[i] > lista[i+1]:
            aux = lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = aux

print(lista)



