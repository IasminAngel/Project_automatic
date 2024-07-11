# pyautogui -> serve para justamente automatização de processos, qualquer tarefa
# Projeto criado para automatizar tarefas no computador
# Necessário fazer instalação do pip install pyautogui

# Pandas utiliza muito base de dados, qual normalmente quando faz códigos seguintes, é bom baixar numpy openpyxl
# pip install pandas numpy openpyxl

# https://dlp.hashtagtreinamentos.com/python/intensivao/login

# commands - # pyautogui.click
# pyautogui.write
# pyautogui.press

import pyautogui 
import pandas
import time

# Pausa entre comandos
pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)

# Essas posições de click apenas usando pois estava com três abas abertas

pyautogui.click(x=858, y= 674)

time.sleep(2)

pyautogui.click(x=767, y= 17)


link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")

# Demora de 3 segundos para entrada
time.sleep(3)

pyautogui.click(x=795, y=411)
pyautogui.write("Meu email teste")
pyautogui.press("tab")
pyautogui.write("Minha senha teste")
pyautogui.press("enter") # opção se o site aceitar entrar com enter, caso não, fazer comando com click

tabela = pandas.read_csv("produtos.csv")
print (tabela)

# MANTER DENTRO DO TAB POIS O PYTHON IDENTIFICA POR IDENTAÇÃO ! ENTÃO O PANDAS VAI IDENTIFICAR QUE ELE TEM QUE REPETIR OS PROCESSOS
# Toda lista de informação em Python é dita em colchete
# no codigo abaixo, tbm é permitido aplicar o codigo todo numa linha só, ficando: pyautogui.write(tabela.loc[linha,""])

for linha in tabela.index:
    # Código do produto
    pyautogui.click(x=768,y=289)

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # Marca do produto
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    # Tipo do produto
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    # Categoria do Produto
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    # Preço do produto unitário
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    # Custo do produto
    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    # OBS
    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    pyautogui.press("enter")
    pyautogui.scroll(5000)