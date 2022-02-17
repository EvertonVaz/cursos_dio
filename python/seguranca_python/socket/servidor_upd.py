import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket created successful')

host = 'localhost'
port = 5432

s.bind((host, port))
message = '\nServer: Hello client'

while 1:
    data, end = s.recvfrom(4096)

    if data:
        print('Server sending mensage')
        s.sendto(data + (message.encode()), end)