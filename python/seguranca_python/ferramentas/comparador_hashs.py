import hashlib

archive1 = 'a.txt'
archive2 = 'b.txt'

hash1 = hashlib.new('ripemd160')
hash1.update(open(archive1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(archive2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f'The archive: {archive1} is different the {archive2}')
    print(f'The hash of the {archive1} is: {hash1.hexdigest()}')
    print(f'The hash of the {archive2} is: {hash2.hexdigest()}')
else:
    print(f'The archive: {archive1} is equal the {archive2}')
    print(f'The hash of the {archive1} is: {hash1.hexdigest()}')
    print(f'The hash of the {archive2} is: {hash2.hexdigest()}')