from CursoEmVideo.Mundo03_Estruturas_Compostas.Exercicios.exercicios_modulo.exe115_modulo.lib.interface import *
from CursoEmVideo.Mundo03_Estruturas_Compostas.Exercicios.exercicios_modulo.exe115_modulo.lib.arquivo import *
from time import sleep

# Verificar se arquivo existe, senão cria:
arq = 'cadastro_pessoas.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo.
        lerArquivo(arq)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa.
        cabecalho("NOVO CADASTRO")
        nome = str(input("Nome: "))
        idade = leia_int(("Idade: "))
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabecalho("Saindo do sistema... Até logo")
        break
    else:
        print("\033[31mERRO! Digite uma opção válida!\033[m")
    sleep(2)


