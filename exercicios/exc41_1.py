# Site https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial='06-01-2023',dataFinalCotacao='07-30-2023')?$top=100&$format=json&$select=cotacaoVenda
# Com base na URL acima, acesse todos os valores de dolares entre 01/08/2023 a 31/08/2023 via request HTTP, calcule a media de venda do dolar neste período e mostre na tela

import requests
import json

print("Cliente HTTP iniciado")
print("Conectando no servidor")

resp = requests.get("https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarPeriodo(dataInicial='08-01-2023',dataFinalCotacao='08-31-2023')?$top=100&$format=json&$select=cotacaoVenda") 

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