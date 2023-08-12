# Funções PARTE 2 - Exercício: Analisando e gerenciando Dicionários

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas de alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    resp = dict()
    for nota in n:
        resp['total'] = len(n)
        resp['maior'] = max(n)
        resp['menor'] = min(n)
        resp['media'] = sum(n)/resp['total']
        if sit == True:
            if resp['media'] < 5:
                resp['situação'] = 'RUIM'
            elif resp['media'] < 7:
                resp['situação'] = 'RAZOÁVEL'
            else:
                resp['situação'] = 'BOA'
    return resp


# Programa principal
resp = notas(5.5, 9.5, 10, 6.5, 8.5, sit=True)
print(resp)