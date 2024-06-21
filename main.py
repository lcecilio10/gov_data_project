from src.extract import govApi
from src.transform import despesas_json_to_parquet
import time

## Função main para orquestrar a execução da extração. A ideia aqui é colocar como input o range d e data
## a ser observado e se queremos limite de paginação pela API ou não.

def main():

    print("======= Transparência GOV BR Extractor ======= \n")
    print("This tool is able to simplify, organize and scale extractions \
          from the Brazilian Government API from multiple endpoints")
    print('Please, provide your expected date range: ')

    start_month_year = str(input('Start Year Month (MM/YYYY): ' ))
    end_month_year = str(input('End Year Month (MM/YYYY): ' ))
    page_limit = int(input('Define a API pagination limit. Set page limit < 0 for full extraction.'))

    if page_limit < 0:
        page_limit = None

    ## Aqui embaixo distribuindo os parametros para a função
    gov_api = govApi()
    gov_api.get_all_public_spent_data(start_year_month=start_month_year, end_year_month=end_month_year, page_limit=page_limit)
    time.sleep(3)
    despesas_json_to_parquet()

if __name__ == '__main__':
    main()

    