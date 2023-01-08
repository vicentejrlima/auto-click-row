# Auto Click Row (ACR)

O ACR busca em um banco de dados ou lista as palavras para serem clicadas nas linhas das tabelas do navegador

## 🚀 Começando

### 📋 Pré-requisitos

Python
WebDriver Chromium

### 🔧 Instalação

Tenha certeza de ter os pré-requisitos e execute:

copie nosso repositório:
```
gh repo clone vicentejrlima/auto-click-row
```

intale as dependencias nescessárias:

```
$ pip install -r requirements.txt
```

## ⚙️ Executando os testes

execute o script:
```
python .\marcar.py
```
### 🔩 Analise os testes de ponta a ponta

pega da tabela oq deve ser buscado.
```
tabela = pd.read_excel('db.xlsx', dtype=str)
```
Transforma em lista simples 
```
itens = tabela['NOME'].tolist()
```
a tag 'label' é onde está o texto, nossa lista 'itens' é enviada para a função checkTab.
```
checkTab(td='label', items=itens)
```

### ⌨️ E testes de estilo de codificação

a função checkTab( ) é toda configuravel:

```
checkTab(site = f'file:///{os.getcwd()}/linhas.html', rowtab = '//*[@id="table-grid"]/tbody/tr', items = '', col = 3, td = '' )
```
argumentos:
```
site = f'seu site' 
```
```
rowtab = 'Xpath da linha da tabela'
```
```
items = 'lista a ser buscada'
```
```
col = número da coluna a ser vasculhada
```
```
td = 'onde está o texto na célula'
```

## 📦 Implantação

Para quem precisa selecionar ou clicar em um grande número de dados

## 🛠️ Construído com

* [Python](https://www.python.org/) - dispensa apresentações
* [Selenium](https://selenium-python.readthedocs.io/) - Framework portátil para testar aplicativos web 
* [Pandas](https://pandas.pydata.org/docs/) - Biblioteca Python que fornece ferramentas de análise de dados e estruturas de dados
* [Rich](https://rich.readthedocs.io/en/stable/introduction.html) Biblioteca que deixa o terminal lindão

## 🖇️ Colaborando

há vagas... 

## 📌 Versão

Versão Beta. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/vicentejrlima/auto-click-row.git). 

## ✒️ Autor

* **Dev** - *Trabalho Inicial - Portifólio* - [Vicente Lima](https://github.com/vicentejrlima)

## 📄 Licença

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎁 Agradecimentos

* "Até aqui nos ajudou o Senhor." (1 Samuel, 7:12) :innocent:;

---
por [Vicente Lima](https://github.com/vicentejrlima) :bowtie:
