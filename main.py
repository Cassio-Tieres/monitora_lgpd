import requests
import pandas as pd

db = pd.read_csv('clientes_sites.csv')
count = 0
counterUrlErr = 0

listaSemLGPD = []
urlsComProblema = []

def getLGPD():
    global count, counterUrlErr, listaSemLGPD, urlsComProblema
    indisponiveis = []  # URLs para serem ignoradas

    for site in db['CLIENTE']:
        if site in indisponiveis:
            continue
        try:
            lgpd = f'https://{site}/politica-de-privacidade'
            response = requests.get(lgpd)
            if response.status_code != 200:
                count += 1
                print(f'Resposta do servidor: {response.status_code}; Site: {site}')
                print('------------------------------')
                listaSemLGPD.append(site)
        except Exception as e:
            print(f'Site: {site} apresentando um erro. Erro: {e}')
            counterUrlErr += 1
            urlsComProblema.append(site)
            continue

    print(f'TOTAL DE SITES SEM POLITICA DE PRIVACIDADE: {count}')
    print(f'TOTAL DE URLs COM ALGUM TIPO DE PROBLEMA: {counterUrlErr}')

getLGPD()

print("SITES SEM POLÍTICA DE PRIVACIDADE:")
print('\n'.join(listaSemLGPD))

print("SITES COM ALGUM PROBLEMA DE CARREGAMENTO (INDEPENDENTE DE QUAL SEJA O PROBLEMA):")
print('\n'.join(urlsComProblema))
