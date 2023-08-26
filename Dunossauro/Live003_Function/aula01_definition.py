# Funções #1 - Definindo funções

# 1-Função nomeada
def minha_funcao():
    return 'Oi'

print(minha_funcao())

# 2-Função anônima

#Opção 1:
anonima = lambda: 'oi - opção1 '
print(anonima())

#Opção 2:
print(lambda: 'teste opção 2')

# 3-Função classe

class FuncaoClasse:
    def __call__(self):
        return 'Oi - Função Classe'

print(FuncaoClasse()())
minha_classe_funcao = FuncaoClasse()
print(minha_classe_funcao())
