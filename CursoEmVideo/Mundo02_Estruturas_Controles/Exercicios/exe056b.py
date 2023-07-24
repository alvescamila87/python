#estrutura de repetição: analisador completo

soma = 0
maior_idade = 0
menor_idade = 0

for pessoa in range(1,5):
    print('------ {}ª PESSOA ------'.format(pessoa))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()

    # Identificar a média de idade do grupo de pessoas
    soma += idade
    media = soma / pessoa
    
    # Identificar a idade da pessoa mais velha do grupo de pessoas
    if pessoa == 1 :
        maior_idade = idade
        menor_idade = idade
        nome_pessoa_maior = nome.upper()
        nome_pessoa_menor = nome.upper()
    else:
        if idade > maior_idade:
            maior_idade= idade
            nome_pessoa_maior = nome.upper()
        else:
            menor_idade = idade
            nome_pessoa_menor = nome.upper()

print("A média da idade do grupo é de {:.1f} anos.".format(media))
print("A pessa mais velha tem {} anos e se chama {}.".format(maior_idade, nome_pessoa_maior))
print("A pessa mais nova tem {} anos e se chama {}.".format(menor_idade, nome_pessoa_menor))

        

