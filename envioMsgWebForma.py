import selenium
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

conversas = ["Xavier CEAP", "Rodolfo CEAP"]
mensagem="""Aaaaadas
asdasd
asdasd
asdasddas"""


servico = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=servico)

url = "https://web.whatsapp.com/"
driver.get(url)
time.sleep(3)

logado=False
while logado == False:
    try:
        pesquisa = driver.find_element(By.XPATH, '//*[@id="side"]/div[1]/div/div/div[2]/div/div[2]')
    except:
        time.sleep(5)
        continue
    
    break

for i in range(len(conversas)):
    pesquisa.send_keys(conversas[i])
    time.sleep(1)
    conversa = driver.find_element(By.XPATH, '//*[@id="pane-side"]/div[1]/div/div/div[4]')
    conversa.click()
    time.sleep(1)
    campodetexto = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div/p')
    campodetexto.send_keys(mensagem)
    time.sleep(1)
    enviar = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    enviar.click()
    time.sleep(1)

time.sleep(1)
    
    