import socket

cli = socket.socket()

cli.connect(('127.0.0.1', 8899))

cli.send(b'hello')
data = cli.recv(1024)
print(data)

cli.close()
