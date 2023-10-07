#Faça um programa que peça um número ao usuário e calcule a progressão geométrica de 1 até este número, assumindo a razão como sendo 3. Utilize recursividade para executar esta atividade an = a1.qn−1
def pg(numero):
    return pg(numero) * 3

numero = int(input('Digite um número: '))

for i in range(numero):
    print(pg(i))