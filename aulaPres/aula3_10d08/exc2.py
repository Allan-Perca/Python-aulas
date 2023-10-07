# def funcao():
#     print("ERROR")
#     print(funcao())

# funcao() #Estoura a memoria

def soma (a,b):
    soma = a + b
    return soma

print("Programa de soma de dois numeros")

print("Digite um numero")
n1 = int(input("> "))
print("Digite um numero")
n2 = int(input("> "))

print(soma(n1, n2))
