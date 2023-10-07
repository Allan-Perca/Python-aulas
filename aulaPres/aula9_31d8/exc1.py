#Biblioteca json transforma o texto em objeto ou lista/dict
import json 

# d = {
#     "nome": "João Silva",
#     "ra": "11111",
#     "nota1": 6.4,
#     "nota2": 5.6
# } #Dicionario normal objs

# as aspas simples demonstram q é um texto, não da pra extrair info
texto = '''{
    "nome": "João Silva",
    "ra": "11111",
    "nota1": 6.4,
    "nota2": 5.6
}'''

obj = json.loads(texto) #desse objeto da pra extrair
print(obj)
print("Nota: ", obj["nota1"])

# Transforma a lista em texto
lista = ["Joao", "Maria", "Alfredo"]
texto_lista = json.dumps(lista)
print("Lista: ", texto_lista)














