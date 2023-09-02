# 1) Importar módulos built-in:

# Listar arquivos dentro de diretório
import glob

# Módulo de sistema operacional
import os

# Módulo para compactar arquivos dentro do python (arquivo .zip)
import zipfile

# 2) Diretório de trabalho atual
os.getcwd()

# 3) Listar arquivos .txt
for file in glob.glob("ArquivosAulas/*txt"):
    print(file)

# 4) Compactar arquivos .txt
with zipfile.ZipFile('arquivos_txt.zip', 'w') as file_zip:
    for file in glob.glob("ArquivosAulas/*txt"):
        file_zip.write(file)

# 5) Compactar arquivos .csv
with zipfile.ZipFile('arquivos_csv.zip', 'w') as file_zip:
    for file in glob.glob('ArquivosAulas/*csv'):
        file_zip.write(file)

# 6) Compactar todos os arquivos
with zipfile.ZipFile('arquivos_gerais.zip', 'w') as file_zip:
    for file in glob.glob("ArquivosAulas/*"):
        file_zip.write(file)