#Servidor teste 
import socket

HOST = "127.0.0.1"
PORT = "20000"

print("Servidor iniciado")

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Servidor criado")

servidor.bind((HOST, PORT))

servidor.listen()

print("Servidor aguardando conexão")

conn, addr = servidor.accept()

print("Cliente está conectado: ", addr)

conn.sendall("Bem vindo\r\n")

while True:
    data = conn.recv(1024)
    print(data)


conn.close()