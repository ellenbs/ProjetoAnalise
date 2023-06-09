import requests
from bs4 import BeautifulSoup

url = 'http://portal.mec.gov.br/pec-g/cursos-e-instituicoes'

response = requests.get(url)
content = response.content

soup = BeautifulSoup(content, 'html.parser')

div = soup.find('div', class_='item-page')
links = div.find_all('a')

with open('universidades.txt', 'w') as file:
    for link in links:
        url = link['href']
        file.write(url + '\n')
