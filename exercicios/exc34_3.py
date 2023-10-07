#Crie um programa que solicite ao usuário para que informe uma quantidade de termos, que deverá ser um número entre 1 e 100. Em seguida o programa deve mostrar na tela a sequencia de Fibonnacci com a quantidade de termos informada pela usuário. Utilize recursividade para resolver este problema. 

# def fibonnacci(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonnacci(n-1) + fibonnacci(n-2)

# print("Digite uma quantidade de termos entre 1 e 100")
# n = int(input("> "))

# for i in range(n):
#     print(fibonnacci(i))

def fibonnacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonnacci(n-1) + fibonnacci(n-2)

# def fibonnacci(n):
#     if n > 1:
#         return fibonnacci(n-1) + fibonnacci(n-2)
#     return n
    
print("Digite uma quantidade de termos entre 1 e 100")
n = int(input("> "))

for i in range(1, n+1):
    print(fibonnacci(i))













