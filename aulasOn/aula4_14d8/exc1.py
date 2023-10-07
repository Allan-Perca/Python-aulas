def fatorial(numero):
    if numero == 2:
        return 2
    else:
        return numero * fatorial(numero - 1)
    
print("Inicio programa de fatorial")
print("Digite um numero entre 1 e 100")
numero = int(input("Digite um numero: "))
print("fatorial ", numero,": " ,fatorial(numero))
