import os
from time import sleep

with open('hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()
    for ip in dump:
        print(f'Verificando ip: {ip}')
        print('-' * 60)
        os.system(f'ping -n 2 {ip}')
        print('*' * 60)
        sleep(1)

print(dump)