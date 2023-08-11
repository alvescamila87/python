# Estrutura de dados composta: Dicionários {}
# Tem Índices por literais personalizáveis
# Elementos / Chaves / Keys

dados = dict()
dados = {"nome":"Camila", "idade": 35}
print(dados) # nome da estrutura
print(dados["nome"]) # nome do primeiro elemento (chave)
print(dados["idade"]) # nome do primeiro elemento (chave)

# Adicionar elementos (chaves)
dados["sexo"] = "M"
print(dados) 

# Remover elementos (chaves)
del dados["idade"]
print(dados) 

# Dicionário para guardar filmes

filme = {"titulo": "Star Wars",
         "ano": 1977,
         "diretor": "George Lucas"        
        }

print(filme)

# Retornar valores do dicionário (conteúdo)
print(filme.values())

# Retornar elementos / chaves / keys do dicionário (índices)
print(filme.keys())

# Retornar valores e chaves do dicionário (conteúdo e índices)
print(filme.items())

# Fazer laços (parecido com enumerate)
for key, value in filme.items():
    print(f"O {key} é {value}")

# É possível juntar: tuplas, listas e dicionários

locadora = [{"titulo": "Star Wars",
     "ano": 1977,
     "diretor": "George Lucas"
    },
    {"titulo": "Avengers",
     "ano": 2012,
     "diretor": "Joss Whedon"
    },
    {"titulo": "Matrix",
     "ano": 1999,
     "diretor": "Wachowski"
    },
]

# Na lista 'locadora', acessar elemento através pelo índice literal "palavra" (chaves)
print(locadora[0]["ano"])
print(locadora[2]["titulo"])


# NOVA SESSÃO DE DEMONSTRAÇÃO

# Declarar um dicionário:
pessoas = {"nome": "Karoline", "idade": 36, "sexo": "F"}
print(pessoas)
print(pessoas["nome"])
print(pessoas["idade"])
print(pessoas["sexo"])
print(f"A {pessoas['nome']} tem {pessoas['idade']} anos de idade.")

# Keys
print(pessoas.keys())

# Values
print(pessoas.values())

# Items
print(pessoas.items())

# Acessar chaves e valores por laços (FOR)
for k in pessoas.keys():
    print(k)

for k in pessoas.values():
    print(k)

for k in pessoas.items():
    # print NÃO formatado:
    print(k)

for k, v in pessoas.items():
    # print formatado:
    print(f"{k} = {v}")

# Adicionar key
pessoas["peso"] = 58.5
for k, v in pessoas.items():
    print(f"{k} = {v}")

# Alterar key
pessoas["nome"] = "Guanabara"
for k, v in pessoas.items():
    print(f"{k} = {v}")

# Remover key
del pessoas["sexo"]
for k, v in pessoas.items():
    print(f"{k} = {v}")

# Criar dicionário dentro de uma lista

brasil = []
estado1 = {"UF": "Santa Catarina", "Sigla": "SC"}
estado2 = {"UF": "Rio Grande do Sul", "Sigla": "RS"}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(estado1)
print(estado2)

# Acessando as informações do dicionário na lista
print(brasil[0])
print(brasil[1])
print(brasil[0]["UF"])
print(brasil[1]["Sigla"])

# Copiar um dicionário

estado = dict()
brasil = list()

for c in range(0,3):
    estado["uf"] = str(input("UF: "))
    estado["sigla"] = str(input("Sigla: "))
    brasil.append(estado.copy())
print(brasil)

for est in brasil:
    print(est)

# For de fora é da lista
for est in brasil:
    # For de dentro é do dicionário
    for k, v in est.items():
        print(f"{k} = {v}") 

# segunda opção de formatação
for est in brasil:
    for v in est.values():
        print(v, end=" ")
    print()