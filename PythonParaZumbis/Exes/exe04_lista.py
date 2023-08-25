import string

# Opcao1
statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.".lower()

lista_pn = list()

for palavra in statement.split():
    if palavra[0] in "python" or palavra[-1] in 'python':
        lista_pn.append(palavra)

print(lista_pn)

# Opcao2

for c in string.punctuation:
    statement = statement.replace(c, " ")

resp = []
for p in statement.split():
    if p[0] in "python" or p[-1] in 'python':
        resp.append(p)

print(resp)