#estruturas compostas: Contando vogais em Tupla

palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "QUARTO", "ESTUDAR", 
            "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO", "UNIVERSO", "CACHORRO")

for p in palavras:
    print(f"\nNa palavra {p} temos as vogais: ", end="")
    for letra in p:
        if letra.upper() in "AEIOU":
            print(letra, end=" ")