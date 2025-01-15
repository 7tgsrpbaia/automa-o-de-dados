import pyautogui
import time
import pandas as pd


pyautogui.PAUSE = 0.5
pyautogui.press ("win")
pyautogui.write ('chrome')
pyautogui.press ("enter")

pyautogui.write ("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press ("enter")
time.sleep (4)
pyautogui.click (x=838, y=405) 

pyautogui.write ('guhhruizff@gmail.com')
pyautogui.press ('tab') 
pyautogui.write ("mateinobru123")
pyautogui.click (x=941, y=568)
tabela = pd.read_csv("G:\Cursos\PHYNTON\PythonPowerUp\produtos.csv")

print(tabela)
time.sleep(2)
for linha in tabela.index:
    pyautogui.click(x=810, y=292)
    codigo = tabela.loc[linha,'codigo']
    pyautogui.write (str(codigo))
    pyautogui.press('tab')
    marca = tabela.loc[linha,'marca']
    pyautogui.write (str(marca))
    pyautogui.press ('tab')
    tipo = tabela.loc[linha,'tipo']
    pyautogui.write (str(tipo))
    pyautogui.press ('tab')
    categoria = tabela.loc[linha,'categoria']
    pyautogui.write (str(categoria))
    pyautogui.press ('tab')
    preco_unitario = tabela.loc[linha,'preco_unitario']
    pyautogui.write (str(preco_unitario))
    pyautogui.press ('tab')
    custo = tabela.loc[linha,'custo']
    pyautogui.write (str(custo))
    pyautogui.press ('tab')
    obs = tabela.loc[linha,'obs']
    if not pd.isna(obs):
        pyautogui.write (obs)
    pyautogui.press ('tab')
    pyautogui.press ('enter')
    pyautogui.press ('pageup')  
