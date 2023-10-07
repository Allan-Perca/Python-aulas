import socket
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 1000))
serversocket.listen(5) # become a server socket, maximum 5 connections
print("Servidor iniciado - aguardando conexao")
connection, address = serversocket.accept()
print("Cliente conectado")
while True:
    buf = connection.recv(64)
    if len(buf) > 0:
        print(buf, end="")