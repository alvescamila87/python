#funcao como parametro

def dados_pessoais(nome, idade, profissao, funcao_imprime):
    resultado = funcao_imprime(nome, idade, profissao) 
    return resultado

def recebe_dados(nome, idade, profissao):
    return "O nome do usuário é %s, com idade de %d anos de profissao %s." %(nome, idade, profissao)

#opcao de imprimir 1
print(dados_pessoais("Camila",35,"Dev", recebe_dados))

#opcao de imprimir 2
resultado = dados_pessoais("Karoline", 36, "Maquiadora", recebe_dados)
print(resultado)

#nova funcao veiculo

def request_info_carro(marca, modelo, ano, funcao_dados):
    resultado = funcao_dados(marca, modelo, ano)
    return resultado

def response_info_carro(marca, modelo, ano):
    return "O veículo de marca %s, modelo %s e ano fabricação %d encontra-se disponível na loja." %(marca, modelo, ano)

print(request_info_carro("BMW", "X1", 2020, response_info_carro))