#passo a passo da automação
#entar no sistema da empresa
#fazer login 
#importar base de dados
#cadastrar o projeto
#repetir ate a cabar

#pyautogui ferramenta de automação
#pandas manipula  a base de dados
#pip install pyautogui instalar a biblioteca pelo prompt
#pip install pandas numpy openpyxl instalar a biblioteca pelo prompt
import pyautogui
import time
import pandas as pd
#comandos de automação
#pyautogui.click -  clicar
#pyautogui.write - escrever
#pyautogui.press - apertar 
#pyautogui.hotkey - fazer uma atalhho  
#pyautogui.scroll()- rolar 

#abrir o sistema
pyautogui.PAUSE = 1 # espera 1 segundo para cada comando
pyautogui.press("win") # abre o windows 
pyautogui.write("chrome")#escreve chome no windows
pyautogui.press("enter")# aperta enter para abrir o chomre 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #abre o link do site de teste
pyautogui.press("enter")# aperta enter para abiri o site
time.sleep(5)#espera 5 segundos
#cadastrar 
pyautogui.click(x=751,y=470)#clica no local do email
pyautogui.write("email")#digita o email
pyautogui.press("tab")#aperta o tab para ir para a senha
pyautogui.write("senha")#digita a senha
pyautogui.press("enter")#aperta no enter
time.sleep(5)#espera 5 segundos
#inmporat base de dados
tabela=pandas.read_csv("produtos.csv")#le o arquivo cvs na mesma pasta, informação separada por virgula e retorna a informaçao para a variavel

for linha in tabela.index:
    pyautogui.click(x=725, y=323)
    for coluna in tabela.columns:
        if pd.isnull(tabela.loc[linha, coluna]):
            pyautogui.press("tab")
        else:
            pyautogui.write(str(tabela.loc[linha, coluna]))
            pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)