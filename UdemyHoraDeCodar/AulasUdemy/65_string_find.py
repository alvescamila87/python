#manipulação de strings: encontrando palavra em string

frase = "Eu quero encontrar o peixe"

#find procura o índice
print(frase.find("peixe"))

#quando não encontra, retorna "-1"
print(frase.find("Camila"))

#fazendo condicional para ajudar a encontrar se está na frase:

if frase.find("peixe") >= 0:
    print("Encontrei o peixe")

