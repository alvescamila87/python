from aula01_intro_oop import Fila

# Abstração de dado:
supermercado = Fila()
banco = Fila()
padaria = Fila()

# Operação abstrata:

supermercado.entrar("Camila")
banco.entrar("Isabel")
padaria.entrar("Paulo")

print(supermercado.fila)
print(banco.fila)
print(padaria.fila)