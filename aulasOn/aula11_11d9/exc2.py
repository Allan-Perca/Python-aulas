import requests

resposta = requests.get("https://www.climatempo.com.br/")

#print("resposta.text")

texto = str(resposta.text)

i = resposta.text.find('id="current-weather-temperature"')

print("Indice ", texto[i:i + 200])

requests.close()