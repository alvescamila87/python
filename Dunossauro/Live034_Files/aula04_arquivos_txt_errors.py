# Live #34 - Trabalhando com arquivos de texto - ERRORS
# string opcional de como errors de enconding devem ser tratados

# errors strict
print(open('arquivo_teste1.txt', errors='strict').read())

# errors replace
print(open('arquivo_teste1.txt', errors='replace').read())

# errors ignore
print(open('arquivo_teste1.txt', errors='ignore').read())

# errors surrogateescape
print(open('arquivo_teste1.txt', errors='surrogateescape').read())

# errors backslashreplace
print(open('arquivo_teste1.txt', errors='backslashreplace').read())