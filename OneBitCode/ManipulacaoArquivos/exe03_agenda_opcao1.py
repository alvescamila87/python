# Agenda de contatos - Opção 1
import os

nome = str(input("Informe o nome do contato: ")).capitalize().strip()
telefone = str(input("Informe o telefone: [0000-0000] ")).strip()
cidade = str(input("Informe a cidade do contato: ")).capitalize().strip()

# adicionar contato a agenda:
with open("ArquivosAulas/exe03_agenda.csv", "a", encoding="utf-8") as file:
    file.write(f"{nome},{telefone},{cidade}\n")

# listar contatos da agenda:

contatos = []

with open("ArquivosAulas/exe03_agenda.csv", 'r', encoding='utf-8') as file:
    for line in file:
        nome, telefone, cidade = line.rstrip().split(",")
        agenda_contato = dict()
        agenda_contato['nome'] = nome
        agenda_contato['telefone'] = telefone
        agenda_contato['cidade'] = cidade
        contatos.append(agenda_contato)

print(contatos)

for contato in sorted(contatos, key=lambda contatos : agenda_contato['nome']):
    print(f"{contato['nome']} {contato['telefone']} {contato['cidade']}")

# remover/excluir contatos da agenda:
local = 'ArquivosAulas/exe03_agenda.txt'
if not os.path.exists(local):
    print("A lista de contatos está vazia")
with open('ArquivosAulas/exe03_agenda.txt', "w", encoding='utf-8') as file:
    file.write("")

    print("Os contatos foram removidos com sucesso!")
