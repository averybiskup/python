import socket

s = socket.socket()

aq = '172.65.244.248'

my_ip = '192.168.42.21'

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((my_ip, 55940))

s.listen(1)

(client_socket, client_address) = s.accept()
print(client_address, "has connected")

while True:
    data = s.recv(1024)
    print(data)
