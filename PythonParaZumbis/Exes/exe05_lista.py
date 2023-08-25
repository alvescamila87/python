import string

# Opcao1
statement = "The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you.".lower()

for c in string.punctuation:
    statement = statement.replace(c, " ")

lista = []
for p in statement.split():
    if p[0] in "python" or p[-1] in 'python':
        if len(p) > 4:
            lista.append(p)

print("OPÇÃO 1: ", lista)

# Opcao2

for c in string.punctuation:
    statement = statement.replace(c, " ")

def pitonica(palavra):
    for letra in palavra:
        if letra in "python":
            return True
    return False

resp = []
for p in statement.split():
    if pitonica(p) and len(p) > 4:
        resp.append(p)
print("OPÇÃO 2: ", resp)