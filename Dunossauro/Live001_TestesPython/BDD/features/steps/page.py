from behave import step
from selenium import webdriver

driver = webdriver.Chrome()

@step('acessar a pagina "{page}"')
def test_access_page(context, page):
    context.driver.get('http://127.0.0.1:8080/')


@step('deve ser exibido na pagina a string "{string}"')
def test_html(context, string):
    assert string in context.driver.page_source, 'O texto não foi encontrado na pagina'
