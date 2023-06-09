import socket
import requests

with open('universities.txt', 'r') as file:
    urls = file.read().splitlines()


with open('ips2.txt', 'w') as file:
    for url in urls:
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            final_url = response.url
            ip = socket.gethostbyname(final_url.split('//')[1].split('/')[0])
            file.write(f"{ip}\n")
            print(f"A URL {url} está hospedada no servidor com o endereço IP: {ip}")
        except (requests.exceptions.RequestException, socket.gaierror) as e:
            print(f"A URL {url} não pôde ser resolvida para um endereço IP")
