import pandas as pd
from configparser import ConfigParser

## Apenas uma funcão pra converter o que vem daquele endpoint em arquivo Parquet.
## O Parquet preserva os metadados do dataframe e por ser armazenamento colunar, manipular e dar load nele
## em outras ferramentas (no nosso caso o Power BI) fica mais leve

def despesas_json_to_parquet():

    config = ConfigParser()
    config.read('./config.ini')
    json_name = config['DEFAULT']['last_extracted_file']
    json_path = f'./src/raw_data/'+ json_name
    converted_dataframe = pd.read_json(json_path)
    print(f'JSON File successfully loaded. Ready to generate parquet file. (Rows, Columns) = {converted_dataframe.shape}')
    converted_dataframe.to_parquet(f"./src/clean_data/gov_despesas_recursos_{converted_dataframe['anoMes'].min()}_{converted_dataframe['anoMes'].max()}.parquet")

