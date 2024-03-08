# Para instalar o selenium digite no cmd: pip install selenium
# Necessário também baixar o webdriver de acordo com o seu navegador, o chromedriver já está na página do projeto, pode usar ele
# Uso o Chrome, baixei um arquivo no site e colei na pasta do projeto.
from selenium import webdriver # biblioteca que vai abrir no navegador, apertar os botões e dar os htmls
#from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By # Usado para identificar as coisas no site(botões, campos de texto)
from time import sleep # sleep(x) faz o programa aguardar x segundos para prosseguir para a próxima linha de código.
from bs4 import BeautifulSoup # Pega um código html e nos permite usar funções especiais para explorá-lo
import pandas as pd # Usado para criar e manipular Dataframes(objetos que representam planilhas)
import openpyxl # Vai servir como parâmentro na função ExcelWriter, para podermos manipular os arquivos excel(xlsx)

lista_links = [10323, 10325, 10327, 10343, 10345, 10347]
"""
Os links dos resultados seguem o seguinte formato:
'http://qselecao.ifce.edu.br/resultado_nomes.aspx?COD_REGRA_CLASSIFICACAO=XXXXX'
O que muda é apenas o XXXXX, sendo eles um dos números da lista_links, cada link é a tabela de resultados de um curso.
Resolvi criar essa lista para não ter que escrever o http://qselecao... 6 vezes.
"""


"\nOs links dos resultados seguem o seguinte formato:\n'http://qselecao.ifce.edu.br/resultado_nomes.aspx?COD_REGRA_CLASSIFICACAO=XXXXX'\nO que muda é apenas o XXXXX, sendo eles um dos números da lista_links, cada link é a tabela de resultados de um curso.\nResolvi criar essa lista para não ter que escrever o http://qselecao... 6 vezes.\n"

navegador = webdriver.Chrome() 

listaDfPrincipal = [] 

posDfPrincipal = 0 
for i in lista_links: 
    navegador.get('http://qselecao.ifce.edu.br/resultado_nomes.aspx?COD_REGRA_CLASSIFICACAO='+str(i))
    sleep(1) 
    botaoClassificacao = navegador.find_element(By.ID, 'ctl00_ContentPlaceHolderPrincipal_rblOrdenacao_1')
    botaoClassificacao.click() 
    sleep(1)
    soup = BeautifulSoup(navegador.page_source, 'html.parser')
    tabela = soup.find(id='ctl00_ContentPlaceHolderPrincipal_wucResultados1_grvConsulta')
    listaDataframes = pd.read_html(str(tabela))
    listaDfPrincipal.append(listaDataframes[0])
    sleep(1)
    for a in range(8):
        botaoCotas = navegador.find_element(By.ID, 'ctl00_ContentPlaceHolderPrincipal_wucSelecionarCota1_rblCotas_'+str(a+1))
        botaoCotas.click() 
        page = navegador.page_source
        soup = BeautifulSoup(page, 'html.parser')
        tabelaCotas = soup.find(id='ctl00_ContentPlaceHolderPrincipal_wucResultados1_grvConsulta')
        if tabelaCotas != None:
            dfTabelaCotas = pd.read_html(str(tabelaCotas))
            listaDfPrincipal[posDfPrincipal] = pd.concat([listaDfPrincipal[posDfPrincipal], dfTabelaCotas[0]])
    sleep(1)
    posDfPrincipal += 1 
    
navegador.close()

nomesPlanilhas = ['Edificações',  'Eletrotécnica', 'Informática', 'Mecânica Industrial', 'Química', 'Telecomunicações']

posNomes = 0
with pd.ExcelWriter("resultado.xlsx", mode="w", engine="openpyxl", ) as writer:
    for df in listaDfPrincipal:
        df.to_excel(writer, sheet_name=nomesPlanilhas[posNomes], index=False)
        posNomes += 1
# Com isso não será mais necessário criar o arquivo manualmente
