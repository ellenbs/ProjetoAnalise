import socket
import requests

with open('ips.txt', 'r') as file:
    ips = file.read().splitlines()

with open('cloud.txt', 'w') as file:
    for ip in ips:
        try:
            reversed_dns = socket.gethostbyaddr(ip)
            print(reversed_dns)
            file.write(f"{ip} - {reversed_dns}\n")

        except socket.herror as err:
            print(f"O endereço IP {ip} não pôde ser resolvido para um nome")
            file.write(f"{ip} - O endereço IP {ip} não pôde ser resolvido para um nome\n")
            print(f"Erro: {str(err)}")