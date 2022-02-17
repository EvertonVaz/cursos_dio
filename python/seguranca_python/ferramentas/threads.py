from threading import Thread
from time import sleep

def carros(piloto, velocidade):
    trajeto = 0
    while trajeto <= 100:
        print(f'Piloto: {piloto}, Km: {trajeto}\n')
        trajeto+=velocidade
        sleep(0.5)

t_carro1 = Thread(target=carros, args=['Junior', 20])
t_carro2 = Thread(target=carros, args=['Gustavo', 20])
t_carro3 = Thread(target=carros, args=['Everton', 20])

t_carro1.start()
t_carro2.start()
t_carro3.start()