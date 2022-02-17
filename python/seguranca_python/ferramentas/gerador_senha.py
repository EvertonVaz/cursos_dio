import random, string

tamanho = 32

chars = string.ascii_letters + string.digits + string.punctuation + 'çÇ´<>'
rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(tamanho)))