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
    print(item["cotacaoVenda"])
    valor = item["value"]
    soma = soma + valor
media = soma / len(lista)
print(media)