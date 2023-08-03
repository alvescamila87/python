#estrutura de repetição: validação de dados

sexo = str(input("Informe o sexo [M/F]: ")).strip().upper()[0]
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos. Favor informar o seu sexo [M/F]: ")).strip().upper()[0]

print("Sexo {} registrado com sucesso.".format(sexo))
    
    
