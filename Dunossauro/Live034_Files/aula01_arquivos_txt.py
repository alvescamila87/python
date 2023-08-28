# Live #34 - Trabalhando com arquivos de texto

# modo write pode ser implícito ou exemplícito

file = open('arquivo_teste.txt', 'w')
file.write('Teste de escrita de arquivo: Open WRITE!')

# modo read pode ser implícito ou exemplícito

file = open('arquivo_teste.txt', 'r')
print(file.read())

print(file)
print(file.read())
print(file.readlines()) #pula linha

# modo append para inserir informações

file = open('arquivo_teste.txt', 'a')
file.write('\nContinuando escrita no arquivo... WRITE')
file.writelines('\nContinuando de onde parou... WRITELINE')

# modo append com for:

from string import ascii_letters

file = open('arquivo_teste_letras.txt', 'a')
for letra in ascii_letters:
    file.write(f"\n{letra}")