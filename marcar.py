from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pandas as pd
from rich.progress import track
from rich import print
import os


def checkTab(site = f'file:///{os.getcwd()}/linhas.html', rowtab = '//*[@id="table-grid"]/tbody/tr', items = '', col = 3, td = '' ):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    navegador = webdriver.Chrome(options=options)
    navegador.implicitly_wait(6)
    if items == '':
        navegador.close()
        print('[red][b]error:[/b] add an item(s) argument to look for...')
        return 0
    navegador.get(site)
    quant = len(navegador.find_elements(By.XPATH, rowtab))
    for x in track(range(quant),description='clicking on the items...'):
        x = x + 1
        pat = f'{rowtab}[{x}]/td[{col}]/{td}'
        textoo = navegador.find_element(By.XPATH, pat).text
        if textoo in items:
            navegador.find_element(By.XPATH, pat).click()
    print(f'[green][b]Concluded:[/b] {len(items)} items clicked.')
    resp = input('See what was done ??? (y | n): ')
    if resp == 'y' or resp == 'Y':
        for iten in items:
            print(f"[blue]{iten}")
    else:
        pass


if __name__ == "__main__":
    tabela = pd.read_excel('db.xlsx', dtype=str)
    itens = tabela['NOME'].tolist()
    checkTab(td='label', items=itens)


