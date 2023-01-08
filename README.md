# Auto Click Row (ACR)

O ACR busca em um banco de dados as palavras para serem clicadas nas linhas das tabelas do navegador

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

Adicione notas adicionais sobre como implantar isso em um sistema ativo

## 🛠️ Construído com

Mencione as ferramentas que você usou para criar seu projeto

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - O framework web usado
* [Maven](https://maven.apache.org/) - Gerente de Dependência
* [ROME](https://rometools.github.io/rome/) - Usada para gerar RSS

## 🖇️ Colaborando

Por favor, leia o [COLABORACAO.md](https://gist.github.com/usuario/linkParaInfoSobreContribuicoes) para obter detalhes sobre o nosso código de conduta e o processo para nos enviar pedidos de solicitação.

## 📌 Versão

Nós usamos [SemVer](http://semver.org/) para controle de versão. Para as versões disponíveis, observe as [tags neste repositório](https://github.com/suas/tags/do/projeto). 

## ✒️ Autores

Mencione todos aqueles que ajudaram a levantar o projeto desde o seu início

* **Um desenvolvedor** - *Trabalho Inicial* - [umdesenvolvedor](https://github.com/linkParaPerfil)
* **Fulano De Tal** - *Documentação* - [fulanodetal](https://github.com/linkParaPerfil)

Você também pode ver a lista de todos os [colaboradores](https://github.com/usuario/projeto/colaboradores) que participaram deste projeto.

## 📄 Licença

Este projeto está sob a licença (sua licença) - veja o arquivo [LICENSE.md](https://github.com/usuario/projeto/licenca) para detalhes.

## 🎁 Expressões de gratidão

* Conte a outras pessoas sobre este projeto 📢;
* Convide alguém da equipe para uma cerveja 🍺;
* Um agradecimento publicamente 🫂;
* etc.


---
⌨️ com ❤️ por [Armstrong Lohãns](https://gist.github.com/lohhans) 😊
