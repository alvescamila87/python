# Módulos e Pacotes - Exercício: Formatando moedas em python

import moeda

p = float(input("Digite o preço: "))
print(f"A metade de R${p:.2f} é: R${moeda.metade(p):.2f}.")
print(f"O dobro de R${p:.2f} é R${moeda.dobro(p):.2f}.")
print(f"Aumentando em 10%, o temos R${moeda.aumentar(p, 10):.2f}.")
print(f"Diminuindo em 10%, o temos R${moeda.diminuir(p, 10):.2f}.")



