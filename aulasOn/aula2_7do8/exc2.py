#Programa que solicite ao usuario dois numeros e mostre na tela qual é o maior. Crie uma função que receba os dois numeros e retorne o maior deles

def maior_numero(a,b):
    resultado = a if a > b else b
    return resultado

def numeros(a, b):
    if a > b:
        return a
    else:
        return b


print("Digite um numero")
n1 = int(input("> "))
print("Digite um numero")
n2 = int(input("> "))

resultado = numeros(n1,n2)

res2 = maior_numero(n1,n2)

print("O numero maior é: ", resultado)
print("O numero maior2 é: ", res2)

