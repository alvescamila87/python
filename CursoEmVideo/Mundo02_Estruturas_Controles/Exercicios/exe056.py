#estrutura de repetição: analisador completo

soma = 0
maior_idade_homem = 0
menor_idade = 0
total_mulher_20 = 0

for pessoa in range(1,5):
    print('------ {}ª PESSOA ------'.format(pessoa))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()

    # Identificar a média de idade do grupo de pessoas
    soma += idade
    media = soma / pessoa
    
    # Identificar a idade e o nome do homem mais velho
    if pessoa == 1 and sexo in "Mm":
        maior_idade_homem = idade
        nome_homem = nome
    if sexo in "Mm" and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_homem = nome

    # Identificar a quantidade de mulheres com menos de 20 anos
    if sexo in "Ff" and idade < 20:
        total_mulher_20 += 1

print("A média da idade do grupo é de {:.1f} anos.".format(media))
print("O homem mais velho tem {} anos e se chama {}.".format(maior_idade_homem, nome_homem))
print("Ao todo são {} mulheres com menos de 20 anos.".format(total_mulher_20))

        

