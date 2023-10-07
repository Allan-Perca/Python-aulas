def somar(*numeros):
    print("numeros ", numeros)
    total = 0
    for n in numeros:
        total = total + n
    return total

print("Numero 1")
numero1 = int(input())
print("Numero 2")
numero2 = int(input())
print("Numero 2")
numero3 = int(input())

r = somar(numero1, numero2, numero3)
print(r)

