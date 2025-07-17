import json

# Abrindo o arquivo JSON
with open('./morse.json', 'r') as arquivo:
    # Carregando o conteúdo do arquivo JSON para uma variável Python
    dados = json.load(arquivo)

print(dados)