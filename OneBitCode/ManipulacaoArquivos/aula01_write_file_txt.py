# Entrada de dados
name = str(input("Informe o seu nome: ")).capitalize()

# Criar arquivo - Alternativa 1
# file = open('ArquivosAulas/aula01_names.txt', 'a')
# file.write(f"{name}\n")
# file.close()


# Criar arquivo - Alternativa 2: trabalhando com contexto
with open('ArquivosAulas/aula01_names.txt', 'a') as file:
    file.write(f"{name}\n")