#dicionario  

carro = {
    "pneus": 4,
    "portas": 2,
    "motor": 1,
    "janelas": 4
}

print(carro)

#adicionar chave de teto solar true
carro["teto solar"] = 1
print(carro)

#deletar: motor e janelas
del carro["motor"]
del carro["janelas"]
print(carro)
