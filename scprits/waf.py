import subprocess
import time

with open('universities.txt', 'r') as file:
    urls = file.read().splitlines()


with open('waf.txt', 'w') as file:
    for url in urls:

        command = ['wafw00f', url]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        result, error = process.communicate()

        file.write(f'URL: {url}\n')
        file.write(result)
        file.write('\n ---------------- \n ---------------- \n')

        print(result)
        print(error)


        time.sleep(10)