# Pedir dois numero inteiros, calcular media aritmetica e mostrar resultado na tela

# print("Digite 2 numeros")
# n1 = int(input("> "))
# n2 = int(input("> "))
# media = (n1 + n2) / 2
# print("Resultado: ", media)

def calcular_media(a, b): #Função pura
    resultado = (a + b) / 2
    return resultado

print("Digite dois numeros")
n1 = int(input("> "))
n2 = int(input("> "))
media = calcular_media(n1, n2)
print("Media: ", media)







