import requests
import csv

API_KEY = '05c097d87b23e8e8efa01b52f3890549c7f1f83b'
URL_PRODUTOS = 'https://www.bling.com.br/Api/v2/produto/json/'

def obter_produtos():
    headers = {'Authorization': f'Bearer {API_KEY}'}
    parametros = {'pagina': 1}  # Pode ajustar conforme necessário
    
    resposta = requests.get(URL_PRODUTOS, headers=headers, params=parametros)
    
    if resposta.status_code == 200:
        return resposta.json()['retorno']['produtos']
    else:
        print(f'Erro ao obter produtos: {resposta.status_code}')
        print(resposta.json())  # Mostra detalhes do erro
        return None

def salvar_csv(produtos):
    with open('produtos.csv', 'w', newline='') as arquivo_csv:
        campos = ['id', 'nome', 'codigo', 'preco']
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
        
        escritor_csv.writeheader()
        for produto in produtos:
            escritor_csv.writerow(produto['data'])

if __name__ == "__main__":
    produtos = obter_produtos()

    if produtos:
        salvar_csv(produtos)
        print('Produtos salvos com sucesso no arquivo produtos.csv.')
    else:
        print('Não foi possível obter os produtos do Bling.')
