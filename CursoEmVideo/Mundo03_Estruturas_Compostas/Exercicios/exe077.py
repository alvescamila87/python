#estruturas compostas: Contando vogais em Tupla

palavras = ("APRENDER", "PROGRAMAR", "LINGUAGEM", "PYTHON", "CURSO", "QUARTO", "ESTUDAR", 
            "PRATICAR", "TRABALHAR", "MERCADO", "PROGRAMADOR", "FUTURO", "UNIVERSO", "CACHORRO")

for p in palavras: # Analisa cada elemento da tupla 'palavras'
    print(f"\nNa palavra {p} temos as vogais: ", end="")
    for letra in p: # Cada palavra na tupla também é uma lista, então pegar cada letra da palavra 'p'
        if letra.upper() in "AEIOU":
            print(letra, end=" ")