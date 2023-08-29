#Live 016 - Manipulação de arquivos e diretórios - Aula 01

import os
import os.path
import shutil

# 1) Criar diretório:
os.mkdir('exe_01')

# 1.1) Criar validação caso diretório já exista:
if not os.path.exists('exe_01'):
    os.mkdir('exe_01')
else:
    print("O diretório já existe!")

# 2) Criar arquivo vazio dentro do diretorio existente:
file = open('exe_01/xpto.txt', 'w')
file.write("")
file.close()

# ou dessa forma:
with open('exe_01/xpto1.txt', 'w') as file:
    file.write("")

# ainda, dessa forma:

from pathlib import Path
Path('exe_01/xpto1.txt').touch()

# 3) automatizar caminho do diretório:

os.chdir('exe_01')

# 4) copiar arquivos:

shutil.copy('xpto.txt', 'xpto1.txt')
shutil.copy('xpto.txt', 'xpto2.txt')
shutil.copy('xpto.txt', 'xpto3.txt')

# ou pode ser:
for elemento in range(1, 4):
    shutil.copy('xpto.txt', f'xpto_{elemento}.txt')

# 5 ) verificar pasta atual

print(os.getcwd())

# 6) listar o que há no diretório:

arquivos_exercicio = os.listdir('.')

# 7) validar/assertiva os arquivos do diretório:

arquivos_exercicio1 = os.listdir('exe_01/')
print(arquivos_exercicio1)

assert len(os.listdir('exe_01/')) == 4