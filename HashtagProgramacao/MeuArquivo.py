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
ticket_medio = ticket_medio.rename(columns={0: 'Ticket médio'})
print(ticket_medio)

# enviar um email com o relatório (código do stackoverflow)
outlook = win32.Dispatch('outlook.application')
mail = outlook.CreateItem(0)
mail.To = 'alvescamilatest@gmail.com'
mail.Subject = 'Relatório de Vendas por Loja'
mail.HTMLBody = f'''
<p>Prezados,</p>

<p>segue o Relatório de Vendas por Loja.</p>

<h3>Faturamento:</h3>
{faturamento.to_html(formatters={'Valor Final': 'R${:,.2f}'.format})}

<h3>Quantidade vendida:</h3>
{quantidade_produtos.to_html()}

<h3>Ticket médio dos produtos em cada loja:</h3>
{ticket_medio.to_html()}

<p>Qualquer dúvida, estou à disposição.</p>

<p>Att.,</p>
<p>Camila</p>

'''

mail.Send()

print('E-mail enviado!')
