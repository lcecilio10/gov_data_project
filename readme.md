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

## ✍️ Autor <a name = "authors"></a>

- [Lucas Cecilio](https://www.linkedin.com/in/lucas-cecilio-carvalho-b10904178/) - Data Analyst

Atualmente trabalhando com Data Analyst para o Grupo QuintoAndar, tenho grande interesse na área
da tecnologia e desenvolvo projetos pessoais para testar e constantemente evoluir meu conhecimento


