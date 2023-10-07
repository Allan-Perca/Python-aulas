import requests
import json

def achar_mediana():
    ordenada = sorted(cotacoes)
    n = len(ordenada)
    if n % 2 == 0:
        valor_meio1 = ordenada[n // 2]
        valor_meio2 = ordenada[n // 2 - 1]
        valor_meio = (valor_meio1 + valor_meio2) / 2
    else:
        valor_meio = ordenada[n // 2]
    return valor_meio

def achar_moda():
    max = 0
    res = sorted(cotacoes)[0] 
    for i in sorted(cotacoes): 
        freq = sorted(cotacoes).count(i) 
        if freq > max: 
            max = freq 
            res = i
        return res 

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

cotacoes = [item["cotacaoVenda"] for item in lista]

valor_minimo = min(cotacoes)
valor_maximo = max(cotacoes)
print("Minimo ", valor_minimo)
print("maximo ", valor_maximo)

amplitute = valor_maximo - valor_minimo
print("Amplitude = ", amplitute)

mediana = achar_mediana()
print("Mediana = ", mediana)

moda = achar_moda()
print("Moda = ", moda)


