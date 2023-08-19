from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common import by

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.get('https://www.google.com/')
# driver.get('http://127.0.0.1:8080/')
driver.save_screenshot('teste.jpeg')
driver.find_element(By.CLASS_NAME, "gLFyf").send_keys('Programação funcional')
print(dir(driver))
#sleep(5)