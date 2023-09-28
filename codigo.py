# Passo a passo do projeto

# Importando as bibliotecas
import pyautogui
import time

pyautogui.PAUSE = 0.5 # Pausa entre cada comando

# Comandos
# pyautogui.click -> clicar com o mouse 
# pyautogui.write -> escrever um texto 
# pyautogui.press -> apertar uma tecla 
# pyautogui.hotkey -> atalho(combiação de teclas)
# pyautogui.scroll -> núm. positivo sobe(500) e núm. negativo desce(-500)

# Passo 1: Entrar no sistema da empresa
  # https://dlp.hashtagtreinamentos.com/python/intensivao/login

    # 1.1 Abrir o Chrome
pyautogui.press('win')
pyautogui.write('chrome')
pyautogui.press('enter')

time.sleep(5)

    # 1.2 Entrar o link
link = 'https://dlp.hashtagtreinamentos.com/python/intensivao/login'
pyautogui.write(link)
pyautogui.press('enter')

    # 1.3 Esperar o site carregar
time.sleep(5)

# Passo 2: Fazer login
pyautogui.click(x=557, y=359) # campo de email
pyautogui.write('aprendendopython@hotmail.com') 

pyautogui.press('tab') # campo de senha
pyautogui.write('python123456')

pyautogui.press('tab') # botão de login
pyautogui.press('enter')

time.sleep(3)

# Passo 3: Importar a base de dados dos produtos
import pandas # biblioteca que lida com base de dados

tabela = pandas.read_csv('produtos.csv')
print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar um produto
    pyautogui.click(x=622, y=245)

    codigo = tabela.loc[linha, 'codigo'] # Método 1
    marca = tabela.loc[linha, 'marca']
    tipo = tabela.loc[linha, 'tipo']
    categoria = tabela.loc[linha, 'categoria']
    
    # Preencher os campos
    pyautogui.write(str(codigo))
    pyautogui.press('tab')
    pyautogui.write(str(marca))
    pyautogui.press('tab')
    pyautogui.write(str(tipo))
    pyautogui.press('tab')
    pyautogui.write(str(categoria))
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario'])) # Método 2
    pyautogui.press('tab')
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    pyautogui.press('tab')

    obs = tabela.loc[linha, 'obs']
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press('tab') # Botão de enviar
    pyautogui.press('enter')

    pyautogui.scroll(5000)

# Passo 5: Repetir o cadastro para todos os produtos

# Bibliotecas
  # instalar PyAutoGui
    # Abrir o terminal
    # Digitar: pip install pyautogui
    # importar no código: import pyautogui

  # instalar Pandas -> abrir o terminal e digitar: pip install pandas numpy openpyxl
    # Abrir o terminal
    # Digitar: pip install pandas numpy openpyxl
    # importar no código: import pandas



