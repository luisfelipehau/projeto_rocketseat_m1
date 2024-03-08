# pip3 install requests==2.31.0
# https://docs.python.org/3/library/

# Importa a biblioteca requests, um módulo de terceiros, para realizar solicitações HTTP
import requests

# Define a URL para fazer a solicitação HTTP
url = "https://www.example.com"

# Envia uma solicitação HTTP GET para a URL especificada e armazena a resposta
response = requests.get(url)

# Exibe o status code da resposta HTTP
print(f"Solicitação HTTP para {url} retornou o status {response.status_code}")
