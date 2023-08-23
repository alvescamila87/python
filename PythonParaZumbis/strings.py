# Slice:
palavra = 'camila'

if palavra == palavra[::-1]:
    print(f"A palavra: {palavra} é palíndrome, veja: '{palavra[::-1]}'.")
else:
    print(f"A palavra: {palavra} NÃO é palíndrome: '{palavra[::-1]}'.")

# Troca de letra:

palavra = str(input("Informe uma palavra: "))
i = 0
# acumulador de soma, produto (fat) e concatenação (merge)
troca = ""
while i < len(palavra):
    if palavra[i] in 'aeiou':
        troca = troca + "*"
    else:
        troca = troca + palavra[i]
    i = i + 1
print(troca)

# replace

s = "um tigre, dois tigres, três tigres"

# assim NÃO funciona
s.replace("tigre", "gato")
print(s)

# assim funciona!!!
s = s.replace("tigre", "camaleão")
print(s)

# Exercício de string:
# escrever o mês por extenso
# converter o 'mm' para inteiro para poder acessar a lista com os meses por exenso

meses = ['janeiro',
         'fevereiro',
         'março',
         'abril',
         'maio',
         'junho',
         'julho',
         'agosto',
         'setembro',
         'outubro',
         'novembro',
         'dezembro']


data = input("Informe a data dd/mm/aaaa: ").split("/")

dia, mes, ano = data

print(f"Data por extenso: {dia} de {meses[int(mes)-1]} de {ano}.")
