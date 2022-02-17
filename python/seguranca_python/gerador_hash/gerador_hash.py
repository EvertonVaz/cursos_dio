import hashlib

string = input("Digite o texto que você gostaria de transformar em hash\n")

def menu_hashs(string):    
    opcao = int(input('''
    ### MENU - ESCOLHA O TIPO DE HASH ###
    1 - MD5
    2 - SHA1
    3 - SHA256
    4 - SHA512\n
    '''))

    menu = {
        1: "MD5",
        2: "SHA1",
        3: "SHA256",
        4: "SHA512"
    }

    opcoes = {
        1: hashlib.md5(string.encode('utf-8')),
        2: hashlib.sha1(string.encode('utf-8')),
        3: hashlib.sha256(string.encode('utf-8')),
        4: hashlib.sha512(string.encode('utf-8'))
    }


    return opcoes.get(opcao, "Opção Invalida"), menu.get(opcao, "Opção Invalida")


resultado, hash = menu_hashs(string)



print(f"""O texto a ser transformado é: {string}, 
A hash do texto é {resultado.hexdigest()},
O algoritimo usado para transformar o texto em hash foi {hash}""")