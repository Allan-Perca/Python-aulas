#Requisição no servidor com python / requisição http de teste

#import requests 
from urllib import request


print("Cliente HTTP iniciado")
print("Conectando no servidor pudim")

resp = request.get("http://pudim.com.br") 

print("Resposta recebida HEADERS")
print(resp.headers)

print("Dados recebidos em formato: ", resp.headers["Content-Type"])

print("Resposta recebida BODY")
print(resp.text)

