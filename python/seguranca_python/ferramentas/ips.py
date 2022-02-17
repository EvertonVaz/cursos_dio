import ipaddress

ip = '192.168.0.1'

endereco = ipaddress.ip_address(ip)

print(endereco + 256)

ip = '192.168.0.0/32'

rede = ipaddress.ip_network(ip)

print(rede)

for i in rede:
    print(i)