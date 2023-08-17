# CRIAR ARQUIVO E MODIFICAR ARQUIVOS:

cadastro_pessoas = ['Camila', 35, 'Karoline', 36, 'Paulo', 63, 'Isabel', 61]
print(cadastro_pessoas)

'''

'r' -> Usado somente para ler algo
'w' -> Usado somente para escrever algo 
'r+' -> Usado para ler e escrever algo 
'a' -> Usado para acrescentar algo  

'''

# Criar arquivo utilizando 'W' que sempre sobrescreva
with open('cadastro_pessoas.txt', 'w') as arquivo:
    for pessoa in cadastro_pessoas:
        arquivo.write(str(pessoa) + ";")

# Alterando o mesmo arquivo utilizando 'A' que sempre acrescenta (criando append)
with open('cadastro_pessoas.txt', 'a') as arquivo:
    for pessoa in cadastro_pessoas:
        arquivo.write(str(pessoa) + ";")

# Ler arquivo utilizando 'R' imprimindo o valor
with open('cadastro_pessoas.txt', 'r') as arquivo:
    for pessoa in cadastro_pessoas:
        print(pessoa)

# Ler arquivo utilizando 'R' imprimindo o valor
with open('cadastro_pessoas.txt', 'r') as arquivo:
    for pessoa in arquivo:
        print(pessoa)

# Ler e escrever no arquivo utilizando 'R+'
with open('cadastro_pessoas.txt', 'r+') as arquivo:
    for pessoa in arquivo:
        print(pessoa)
    arquivo.write("FIM DO ARQUIVO")