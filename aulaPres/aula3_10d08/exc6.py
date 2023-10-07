#Faça um programa que peça um número ao usuário e calcule a progressão geométrica de 1 até este número, assumindo a razão como sendo 3. Utilize recursividade para executar esta atividade an=a1.qn−1


def progressao(num):
    a1 = 1
    q = 3
    while a1 <= num:
        print(a1)
        a1 = a1 * q
        a1 = progressao(a1)


    

print("Digite um numero")
n1 = int(input("> "))

print(progressao(n1))

