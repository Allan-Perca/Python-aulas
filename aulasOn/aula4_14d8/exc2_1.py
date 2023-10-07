
def pg(numero, q):
    if numero <= 1:
        return 1
    else:
        return q + pg(numero - 1, q)
    

print("Programa que calcula progressão geometrica")

print("Digite o termo")
termo = int(input("> "))

print("Digite a razão")
razao = int(input("> "))

resultado = pg(termo, razao)
print(f"PG do {termo}º elemento com a razão {razao} é: ", resultado)


print("Fim do programa")

