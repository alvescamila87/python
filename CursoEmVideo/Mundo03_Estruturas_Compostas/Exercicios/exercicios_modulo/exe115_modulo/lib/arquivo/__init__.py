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
        print(f"\033[31mHouve um ERRO na criação do arquivo!\033[m")
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
        print(a.read())