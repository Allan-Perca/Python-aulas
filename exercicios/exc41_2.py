# Site https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial='06-01-2023',dataFinalCotacao='07-30-2023')?$top=100&$format=json&$select=cotacaoVenda
# Com base na URL acima, acesse todos os valores de dolares entre 01/08/2023 a 31/08/2023 via request HTTP, calcule a media de venda do dolar neste período e mostre na tela
# Modifique o sistema para pedir que o usuário informe a data de inicio e a data de fim para calcular os dados do dolar. 
import requests
import json

print("Cliente HTTP iniciado")
print("Conectando no servidor")

inicio_dia = input("Informe o dia da data inicial (Exemplo 08): ")
inicio_mes = input("Informe o mes da data inicial (Exemplo 08): ")
inicio_ano = input("Informe o ano da data inicial (Exemplo 2023): ")

final_dia = input("Informe o dia da data final (Exemplo 08): ")
final_mes = input("Informe o mes da data final (Exemplo 08): ")
final_ano = input("Informe o ano da data final (Exemplo 2023): ")

inicio = "{}-{}-{}".format(inicio_mes,inicio_dia, inicio_ano)
final = "{}-{}-{}".format(final_mes, final_dia, final_ano)

endereço = "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial='{}',dataFinalCotacao='{}')?$top=100&$format=json&$select=cotacaoVenda".format(inicio, final)

resp = requests.get(endereço) 

print("Resposta recebida HEADERS")
print(resp.headers)

print("Dados recebidos em formato: ", resp.headers["Content-Type"])

print("Resposta recebida BODY")
print(resp.text)

dados = json.loads(resp.text)
lista = dados["value"]
print(lista)
soma = 0

for item in lista:
    print("Valor: ", item["cotacaoVenda"])
    valor = item["cotacaoVenda"]
    soma = soma + valor
print("Itens: ", len(lista))
media = soma / len(lista)
print("Media: ", media)