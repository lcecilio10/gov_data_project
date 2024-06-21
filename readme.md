<p align="center">
  <a href="" rel="noopener">
 <img width=475px height=270px src="https://www.gov.br/secom/pt-br/central-de-conteudo/manuais/uso-da-marca-do-governo-federal/2023_br_govfederal_marcaoficial_rgb.png" alt="Project logo"></a>
</p>

<h3 align="center">Extração de Dados - GOV RJ</h3>

---

<p align="center"> Projeto desenvolvido por Lucas Cecilio Carvalho em 20/06/2024
    <br> 
</p>

## 📝 Sumário

- [O Projeto](#about)
- [Insights](#insights)
- [Oportunidades](#oportunidades)
- [Autor](#authors)

## 🧐 O Projeto <a name = "about"></a>

O projeto contempla uma extração de API da Transparência do Governo Brasileiro. Acessa-se o
endpoint de *despesas/recursos-recebidos*, passando como parâmetro a para baixar como JSON as respostas da API. 
Após isso,os dados são salvos em Parquet para reter os metadados e garantir melhor performance na etapa posterior.
Os dados extraídos foram analisados no Power BI para exibir os principais insights do período analisado.

Para instalar as libs básicas do projeto, basta ter o Python instalado e instalar os requerimentos do arquivo 
*requirements.txt*.

      pip3 install -r requirements.txt

Depois, rodar acessar a pasta raiz do projeto e rodar o comando:

      python3 main.py

Por final, obter o token de API do governo, renomear o arquivo "config_ini_example.ini" para "config.ini"
e salvar o token no arquivo de configuração na sessão "auth_token"

## 🎈 Insights <a name="insights"></a>
#### Disclaimers : 
- Para elaborar o dashboard, fiz uma extração de Jan/24 a Mai/24.
- O script passa como parâmetro UF = RJ para trazer apenas dados do Estado do RJ

#### Dashboard [Link aqui](https://app.powerbi.com/view?r=eyJrIjoiNDlmNjBlOTctMmI4My00ZDVjLWE4ZWUtYzU4NzIxN2QwODcyIiwidCI6ImFhNDk1ZjJjLWQzN2UtNGI1OC1hYjk1LWJmMDg3NGEzYWRiMiJ9)
O dashboard procura oferecer uma visão descritiva sobre as despesas federais no estado do RJ e facilitar
a extração de informação de uma grande base de dados. As transformações no Power Query são relativamente simples
já que os dados já vem tratados da API. Criei também uma tabela de data para ordernar os meses e uma de medidas
para servir como pastas de medidas.

Alguns quick insights do dash:

- Ao longo de 2024, tivemos 106.49K favorecidos no RJ por recursos recebidos do governo federal, com um total de
R$ 72 bi entre Janeiro e Maio.
- O BNDES representa quase 30% do valor recebimento de recursos federais. Faz sentido já que a sede principal do banco
é no Rio de Janeiro.
- O BNDES, em Abril (em final de Abril as chuvas começaram a impactar o RS) teve um pico de recebimentos federais, aproximadamente 40 % foram de folha de pagamento, e outros 40% de despesas pertinentes ao Ministério do Meio Ambiente
e Mudanças Climáticas (provavelmente recursos emergenciais para problemas oriúndos da catastrofe).
- O Rio de Janeiro, por ser sede de importantes estatais do governo e uma série de instituições federais de ensino,
tal como ter maior demografia que os outros municípios, tem majoritariamente a maior parte do recebimento de recursos,
chegando a importâncias bilionárias de recursos recebidos. Em contrapartida, a cidade vizinha (que tem maior IDH) tem como maior despesa a UFF com R$ 286 Mi recebidos no período de análise.

## 🔮 Oportunidades <a name = "oportunidades"></a>

Fiz esse projeto um pouco rápido já que hoje (21/06) é meu aniversário e estava com uma viagem programada há um tempo.
Portanto, há algumas oportunidades de melhorar o código e a análise do projeto:
- Criei uma ingestão simples de arquivo pra facilitar o desenvolvimento, mas ela pode ser quebrada da seguinte forma : como a gente só salva o JSON após todos os requests serem processados, caso um deles falhe, a extração é cancelada. Com mais tempo eu produtizaria isso da seguinte forma : talvez um Hadoop com o Hive mapeando campos de cada request, que geraria um JSON por request e automaticamente agruparia num tabelão de datalake. Depois com o pandas ou spark, a gente conseguiria processar os dados.
- Traria também dados de anos anteriores, pra fazer comparações históricas year over year ou month over month. Seria
possível também analisar tendências via série temporal, talvez com algum modelo simplificado tipo o ARIMA.

## ✍️ Autor <a name = "authors"></a>

- [Lucas Cecilio](https://www.linkedin.com/in/lucas-cecilio-carvalho-b10904178/) - Data Analyst

Atualmente trabalhando como Data Analyst para o Grupo QuintoAndar, tenho grande interesse na área
da tecnologia e desenvolvo projetos pessoais para testar e constantemente evoluir meu conhecimento


