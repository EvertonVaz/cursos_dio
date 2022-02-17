'''
    Web Scraping
    Um web scraping é uma ferramenta de coleta de dados web, uma forma de mineração que permite a extração de dados de sites da web convertendo-os em informação estruturada para posterior análise

    Bibiotecas 
    BeatifulSoup - é uma biblioteca de extração de dados de arquivos HTML e XML
    requests - permite que vocÊ envie solicitações HTTP em python
'''

from bs4 import BeautifulSoup
import requests

cidade = input('Digite o nome da cidade que você deseja visualizar a temperatura atual: \n').lower()

if cidade.find(' ') > 1:
    cidade = cidade.replace(" ", '-')


# objeto site recebe o conteúdo da requisição http do site
site = requests.get(f'https://www.tempo.com/{cidade}.htm').content

# objeto soup baixando do site o html
soup = BeautifulSoup(site, 'html.parser')

print("Dados coletados do site www.tempo.com para fins de estudos\n")

temperatura = soup.find('span', {'class': "dato-temperatura changeUnitT"})
titulo = soup.title.string

print(titulo[:titulo.find('.')])
print("Temperatura atual: ", temperatura.string)
