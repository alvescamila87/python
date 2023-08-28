from string import ascii_letters

file = open('arquivo_teste_letras.txt', 'a')
for letra in ascii_letters:
    file.write(f"\n{letra}")