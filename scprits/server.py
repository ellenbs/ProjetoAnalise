import subprocess
from urllib.parse import urlparse

with open('universities.txt', 'r') as file:
    urls = file.read().splitlines()

with open('server_dns.txt', 'w') as output_file:
    for url in urls:
        parsed_url = urlparse(url)
        host = parsed_url.netloc

        command = ['curl', '-I', host]
        result = subprocess.run(command, capture_output=True, text=True)

        server_info = ''
        location_info = ''
        for line in result.stdout.splitlines():
            if line.startswith('Server:'):
                server_info = line
            elif line.startswith('Location:'):
                location_info = line

        output_file.write(f'URL: {host}\n')
        output_file.write(f'{server_info}\n')
        output_file.write(f'{location_info}\n')
        output_file.write('\n')