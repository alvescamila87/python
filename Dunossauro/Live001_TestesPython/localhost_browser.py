from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# Inicializar o driver do Selenium
driver = webdriver.Chrome()

# Abrir o Google
# driver.get('https://www.google.com/')
driver.get('http://127.0.0.1:8080/')

# Dar print ao abrir o navegador
driver.save_screenshot('teste.png')



print(driver.page_source)

# Aguardar antes de fechar
# sleep(5)
