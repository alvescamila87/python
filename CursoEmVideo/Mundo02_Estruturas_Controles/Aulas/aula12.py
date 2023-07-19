#Condicoes Aninhadas

nome = str(input("Qual seu nome? "))

if nome == "Camila":
    print("Que nome bonito, {}".format(nome))
elif nome == "Maria" or nome == "Ana":
    print("Seu nome é popular")
else:
    print("Seu nome é bem normal")

print("Tenha um bom dia!")