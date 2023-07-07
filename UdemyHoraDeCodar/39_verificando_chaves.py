#dicionarios - verificando chave valor

dicionario = {
    "objeto": "Pedra",
    "nome": "Onix",
    "idade": 350
}

print(dicionario)

print("nome" in dicionario)
print("sobrenome" in dicionario)


if "nome" in dicionario:
    print("O nome é %s" %(dicionario["nome"]))

if "sobrenome" in dicionario:
    print("existe")