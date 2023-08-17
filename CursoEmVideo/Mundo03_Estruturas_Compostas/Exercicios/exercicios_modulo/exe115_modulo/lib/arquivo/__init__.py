from CursoEmVideo.Mundo03_Estruturas_Compostas.Exercicios.exercicios_modulo.exe115_modulo.lib.interface import *

def arquivoExiste(nome_arquivo):
    try:
        # Abrir arquivo em modo text:
        a = open(nome_arquivo, 'rt')
        # Fechar arquivo:
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True



def criarArquivo(nome_arquivo):
    try:
        # Criar arquivo de texto e, se não existir o arquivo, cria:
        a = open(nome_arquivo, 'wt+')
        # Fechar arquivo:
        a.close()
    except:
        print(f"\033[31mERRO na criação do arquivo!\033[m")
    else:
        print(f"Arquivo '{nome_arquivo}' criado com sucesso!")



def lerArquivo(nome_arquivo):
    try:
        # Ler arquivo:
        a = open(nome_arquivo, 'rt')
    except:
        print(f"\033[31mERRO ao ler o arquivo!\033[m")
    else:
        cabecalho("PESSOAS CADASTRADAS")
        # O 'print' foi comentado para utilizar a próxima linha para formatação dos dados no arquivo, com 'FOR'
        # print(a.read())
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace("\n","")
            print(f"{dado[0]:<30}{dado[1]:>3} anos")
    finally:
        # Fechar arquivo
        a.close()


def cadastrar(nome_arquivo, nome_pessoa="desconhecido", idade_pessoa=0):
    try:
        # Abrir arquivo de texto
        a = open(nome_arquivo, 'at')
    except:
        print(f"\033[31mERRO na abertura do arquivo!\033[m")
    else:
        try:
            a.write(f"{nome_pessoa};{idade_pessoa}\n")
        except:
            print(f"\033[31mERRO na hora de escrever os dados no arquivo!\033[m")
        else:
            print(f"Novo registro de '{nome_pessoa}' adicionado.")
            a.close()