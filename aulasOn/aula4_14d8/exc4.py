def media(*numeros):
    print("numeros ", numeros)
    total = 0
    for n in numeros:
        total = total + n
    media = total / len(numeros)
    return media

print("Programa para calculo de media")

print("Menu")
print("Qual media deseja calcular:")
print("(B)imestre")
print("(A)no")
print("(C)urso")
print("Digite a sua opção:")
opcao = input("> ").upper().strip()[0]

if opcao == "B":
    print("Informe as notas do Bimestre:")
    n1 = float(input("1º nota: \n> "))
    n2 = float(input("2º nota: \n> "))
    n3 = float(input("3º nota: \n> "))
    resultado = media(n1, n2, n3)
    print(f"A media das notas - {n1}, {n2}, {n3} - é = ", resultado)
elif opcao == "A":
    print("Informe as notas do Ano:")
    n1 = float(input("1º nota: \n> "))
    n2 = float(input("2º nota: \n> "))
    n3 = float(input("3º nota: \n> "))
    n4 = float(input("4º nota: \n> "))
    resultado = media(n1, n2, n3, n4)
    print(f"A media das notas - {n1}, {n2}, {n3}, {n4} - é = ", resultado)
elif opcao == "C":
    print("Informe as notas do Curso:")
    n1 = float(input("1º nota: \n> "))
    n2 = float(input("2º nota: \n> "))
    resultado = media(n1, n2)
    print(f"A media das notas - {n1}, {n2} - é = ", resultado)