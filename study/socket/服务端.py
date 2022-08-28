import socket

server = socket.socket()
server.bind(('127.0.0.1', 8899))
server.listen(5)

conn, addr = server.accept()

data = conn.recv(1024)
print(data)

conn.close()
server.close()
