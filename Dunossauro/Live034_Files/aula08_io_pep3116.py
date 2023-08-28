# IO (PEP 3116)
# RawIO: trabalha com arquivos puros
# TextIOBase: trabalha com arquivos de texto
# BufferIOBase: trabalha com buffer
# meta classe: ABC (collection ABC): IO Base e TextIOBase

# type
print(type(open('teste_newline.txt')))

# leitura com with
with open('teste_newline.txt') as file:
    print(file.read())

# para iterar a leiturar, usar o seek.
with open('teste_newline.txt') as file:
    print(file.read())
    file.seek(0)
    print(file.read())
