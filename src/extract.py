import requests
import json
from configparser import ConfigParser
import time

## Esse código tem o objetivo de encapsular as interações com a API da Transparência GOV usando
## Programação Orientada a Objetos (isso facilita que a solução seja produtizada e tenha melhor manutenção)

# Definindo classe
class govApi:

    #Aqui, definindo os atributos da classe. A idéia é iniciar ela já recuperando a informação do URL e do token de API,
    ##que encontra-se armazenada num arquivo. 

    def __init__(self):

        self.config = ConfigParser() 
        self.config.read('./config.ini')
        self.key_name = self.config['DEFAULT']['key_name']
        self.auth_token = self.config.get('DEFAULT', 'auth_token')
        self.base_url = self.config.get('DEFAULT', 'base_url')
    
    ## Sem muito mistério, função para simplificar request pra pegar dados no endpoint despesas/recursos-recebidos

    def get_spent_resources_data(self, params):
        headers = {self.key_name:self.auth_token}
        endpoint = 'despesas/recursos-recebidos'
        url = self.base_url + endpoint
        try:
            req = requests.get(url, headers=headers, verify=True, params=params)
        except:
            print("Error on requesting data ! Check error failed response below: \n")
            print(req.content)
        response = req.json()
        print(f"Data retrieved sucessfully. Status code {req.status_code}")

        return response
    
    ## Aqui, a idéia é iterar na *get_spent_resources_data* até depletar as páginas de dados do endpoint
    ## Concatena-se as resposes JSON numa lista que é submetida por inteiro num único arquivo texto.
    ## Passei como parâmetros os meses de início e fim da extração, e o UF (esse pra reduzir a qtd. de dados,
    ## já que esse endpoint em específico tá na casa das 30 mil páginas e a API tem limitação de request por minuto)
    ## OBS: setei o script para guardar o nome do arquivo da ultima extração

    def get_all_public_spent_data(self, start_year_month, end_year_month, page_limit = None):

        page = 1
        all_data = []

        while True:
            print(f"Extracting JSON from page {page}...")
            payload = {'uf':'RJ', 'mesAnoInicio':start_year_month, 'mesAnoFim':end_year_month, 'pagina':page}
            time.sleep(0.65)
            response = self.get_spent_resources_data(params=payload)

            if not response or (page >= page_limit and page_limit != None):
                break
            all_data.extend(response)
            page+=1
        with open(f"./src/raw_data/extraction_RJ_{start_year_month.replace('/','')}_{end_year_month.replace('/','')}_{page}.json", 'w') as f:
            json.dump(all_data, f, ensure_ascii=False, indent=4)
        print(f"Data succesfully saved on file extraction_RJ_{page}.json")
        parser = ConfigParser()
        parser.read('./config.ini')
        parser['DEFAULT']['last_extracted_file'] = f"extraction_RJ_{start_year_month.replace('/','')}_{end_year_month.replace('/','')}_{page}.json"
        with open('./config.ini', 'w') as configfile:
            parser.write(configfile)
