import requests

resposta = requests.get("https://olinda.bcb.gov.br/olinda/service/PTAX/versions/v1/odata/Currencies?"+"/$format=json&$top=10", {"$format": "json", "$top": "10"})

print(resposta.status_code)

moedas = resposta.json()["value"]

for moeda in moedas:
    print("Symbolo: ", moeda["simbolo"])

