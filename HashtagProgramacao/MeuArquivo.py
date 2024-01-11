import pandas as pd
import win32com.client as win32

# importar base de dados
tabela_vendas = pd.read_excel('vendas.xlsx')

# visualizar a base de dados
pd.set_option('display.max_columns', None)
print(tabela_vendas)

print('-' * 50)
# faturamento por loja (filtra, agrupa e soma)
faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum()
print(faturamento)

print('-' * 50)
# quantidade de produtos por loja
quantidade_produtos = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum()
print(quantidade_produtos)

print('-' * 50)
# ticket medio por produto em cada loja
ticket_medio = (faturamento['Valor Final'] / quantidade_produtos['Quantidade']).to_frame()
print(ticket_medio)

# enviar um email com o relatório (código do stackoverflow)
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'alvescamilatest@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = '''
Prezados,

segue o Relatório de Vendas por Loja.

Faturamento:
{}

Quantidade vendida:
{}

Ticket médio dos produtos em cada loja:
{}

Qualquer dúvida, estou à disposição.

Att.,
Camila

'''
mail.Send()

print('E-mail enviado!')
