# Live #34 - Trabalhando com arquivos de texto - Enconding
# encode do arquivo a ser lido, formatação suportada
# importante usar quando mexe com arquivo multiplataforma

print(open('arquivo_teste1.txt.', 'r', encoding='windows 1252').read())

file = open('teste_enconding.txt', 'w', encoding='windows 1252')
file.write('\n Festa São João')

print(open('teste_enconding.txt').read())


# quando não informa o enconding, o mesmo fica como 'none' e o python usa o 'locale.getpreferredencoding()' do shell 'UTF-8'



