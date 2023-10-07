def fatorial(numero):
    print(numero)
    if numero <= 2:
        return 2
    else:
        return numero * fatorial(numero - 1)


print(fatorial(5))