import itertools

string = input('Palavra a ser permutada: ')
resultado = itertools.permutations(string, 3)

for i in resultado:
    print(''.join(i))