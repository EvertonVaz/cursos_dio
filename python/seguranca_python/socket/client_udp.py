import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Socket created successful')

host = 'localhost'
port = 5432
message = 'Hello server'

try:
    print(f'Initializing connection')
    s.sendto(message.encode(), (host, port))

    data, server = s.recvfrom(4096)
    data = data.decode()
    print(f'Client: {data}')
finally:
    print('Client: Connection closed')
    s.close()