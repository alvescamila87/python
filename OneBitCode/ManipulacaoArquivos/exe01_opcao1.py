import os

# validação de diretório
os.chdir('ArquivosAulas')
diretorio = 'exe01_cities.txt'
if not os.path.exists(diretorio):
    os.mkdir(diretorio)
else:
    print("O diretório já existe!")

# leitura de linhas
with open(diretorio, 'r') as file:
    qtd_linhas = len(file.readlines())
print(f"O arquivo '{diretorio}' possui {qtd_linhas} linhas.")


with open(diretorio, 'r') as file:
    data = file.readlines()[200]
    print(f"A escolhida linha tem a cidade de: {data}")


