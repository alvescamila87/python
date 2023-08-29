#Live 016 - Manipulação de arquivos e diretórios - Aula 03

import os
import os.path
import shutil
from pathlib import Path



# criando diretório do exercício da aula:
# os.mkdir('exe_03')

# setando o diretório como padrão:
os.chdir('exe_03')

# criando as pastas no diretório:
for el in range(1, 11):
    diretorio = f"pasta_{el}"
    if not os.path.exists(diretorio):
        os.mkdir(diretorio)

# conferindo arquivos no diretório:
arquivos_exercicio3 = os.listdir('.')
print(arquivos_exercicio3)

# criando arquivos dentro de cada pasta
# for path in arquivos_exercicio3:
#     Path(f'{path}/arquivo_1.txt').touch()
#     Path(f'{path}/arquivo_2.txt').touch()

# ou dessa forma:
# for path in arquivos_exercicio3:
#     Path(os.path.join(path, 'arquivo_1.txt')).touch()
#     Path(os.path.join((path, 'arquivo_2.txt')).touch()

# imprima a estrutura do diretório:
# print(os.walk('.'))

for valor in os.walk('.'):
    print(valor)