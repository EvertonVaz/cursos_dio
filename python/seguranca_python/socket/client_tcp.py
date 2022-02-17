import socket
import sys

def main(ip, porta):
    # tentar uma conexão tcp ip
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('Connection failed!')
        print(f'Error: {e}')
        sys.exit()

    print('Socket created as successful')

    HostAlvo = ip
    PortaAlvo = porta

    try:
        s.connect((HostAlvo, int(PortaAlvo)))
        print(f'Client TCP has been connected on Host: {HostAlvo} and Port: {PortaAlvo}')
        s.shutdown(2)
    except socket.error as e:
        print(f"Don't possible to connect on Host: {HostAlvo} and Port: {PortaAlvo}")
        print(f"Error> {e}")
        sys.exit()

if __name__ == '__main__':
    main('google.com', 80)
    main('teste.com.br', 80)
    main('dhaosidhas.com.br', 80)

