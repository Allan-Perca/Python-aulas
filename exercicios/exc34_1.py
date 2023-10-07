#Faça um programa que peça um número ao usuário e calcule seu fatorial utilizando função recursiva. Para facilitar vamos assumir que o fatorial de qualquer numero abaixo de 2 seja igual a 2. E para não estourar a memoria, ele não poderá calcular números fatoriais acima de 64

def fatorial(numero):
    if numero <= 2:
        return 2
    else:
        return numero * fatorial(numero - 1)

print("Digite um numero entre 2 e 64")
n1 = int(input("> "))

if (2 < n1 < 64):
    print(fatorial(n1))
else:
    print("Numero não permitido")
