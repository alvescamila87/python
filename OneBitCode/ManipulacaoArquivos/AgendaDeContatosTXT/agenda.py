# Projeto Camila
import os

def adicionar_contatos():
    """
    Função para adicionar contatos a um arquivo .txt
    """
    nome = str(input("Informe o nome do contato: ")).capitalize().strip()
    endereco = str(input(f"Informe o endereço de {nome}: ")).capitalize().strip()
    cidade = str(input(f"Informe a cidade de {nome}: ")).capitalize().strip()
    uf = str(input(f"Informe a UF de {cidade}: ")).upper().strip()
    tel = str(input(f"Informe o telefone de {nome}: ")).strip()

    contato = f"Nome: {nome}\nEndereço: {endereco}\nCidade: {cidade}\nUF: {uf}\nTelefone: {tel}\n"

    with open("arquivo_agenda_contatos.txt", "a", encoding="utf-8") as file:
        file.write(contato)


def visualizar_contatos():
    """
    Função para visualizar os contatos de um arquivo .txt
    """
    local = "arquivo_agenda_contatos.txt"
    if not os.path.exists(local):
        print("A lista de contato está vazia!")
        return
    with open("arquivo_agenda_contatos.txt", "r", encoding="utf-8") as file:
        contatos = file.read()
    print("Lista de contatos")
    print(contatos)


def deletar_contatos():
    """
    Função para deletar os contatos de um arquivo .txt
    """
    local = "arquivo_agenda_contatos.txt"
    if not os.path.exists(local):
        print("A lista está vazia!")
        return
    with open("arquivo_agenda_contatos.txt", "w", encoding="utf-8") as file:
        file.write("")

    print("Os contatos foram removidos com sucesso!")


def linha(tamanho=50):
    """
    Função para imprimir uma linha padrão.
    :param tamanho: parâmetro opcional, com tamanho padrão de 50 caracteres.
    """
    return '-' * tamanho


def cabecalho(texto):
    """
    Função para imprimir uma cabeçalho com texto centralizado, utilizando a função linha.
    :param texto: parâmetro obrigatório, que recebe texto para ser centralizado no cabeçalho.
    """
    print(linha())
    print(texto.center(50))
    print(linha())


def menu(lista):
    cabecalho("MENU PRINCIPAL")
    contador = 1
    for item in lista:
        print(f"{contador} - {item}")
        contador += 1
    print(linha())
