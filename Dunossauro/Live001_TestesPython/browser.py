# Automate the search box from Google using Selenium in Python

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Inicializar o driver do Selenium
driver = webdriver.Chrome()

# Abrir o Google
driver.get('https://www.google.com/')

# Localizar o campo de pesquisa e inserir a consulta de pesquisa
search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')

# Inserir a consulta de pesquisa
search_box.send_keys("Programação funcional")

# print(dir(driver))

# Aguardar antes de fechar
# sleep(5)

# Pressionar a tecla Enter para realizar a pesquisa
search_box.send_keys(Keys.RETURN)

# Fechar o driver após a pesquisa (Alternativa para manter o navegador aberto e pesquisando)
search_box = str(input("Informe algo para fechar o browser: "))

