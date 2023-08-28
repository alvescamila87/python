# Live #34 - Trabalhando com arquivos de texto - NEWLINE
# controla como o 'unversal newlines' (PEP278) vai funcionar
# \n padr�o linux
# \n padr�o mac
# \r\n padr�o windows

print(open('teste_newline.txt', newline="").readlines())
print(open('teste_newline_n.txt', ).readlines())