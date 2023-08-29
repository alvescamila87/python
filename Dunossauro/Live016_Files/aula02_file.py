#Live 016 - Manipulação de arquivos e diretórios - Aula 02

import os
import os.path
import shutil
from pathlib import Path


# Criando diretório
# os.mkdir('exe_02')

# Manter caminho do diretório
os.chdir('exe_02')

# Criando arquivos
# for el in range(1,11):
#     Path(f'live_{el}.txt').touch()

# Listando arquivos do diretório
arquivos_exercicio2 = os.listdir('.')
print(arquivos_exercicio2)

# list comprehension para listar somente os arquivos 'live_':
lista = [f for f in os.listdir('.') if f.startswith('live_')]

# partir lista de aquivos:

for _file in lista:
    print(_file.partition('_'))

# pegar o 3º elemento [2] com o 1º valor [0] e removendo arquivos <= 5

for _file in lista:
    if int(_file.partition('_')[2][0]) <= 5:
        os.remove(_file)

# renomear/alterar arquivos restantes
lista = [f for f in os.listdir('.') if f.startswith('live_')]
print(lista)

for valor, el in enumerate(sorted(lista), 1):
    shutil.move(el, f'live_{valor}')

lista = [f for f in os.listdir('.') if f.startswith('live_')]
print(lista)




