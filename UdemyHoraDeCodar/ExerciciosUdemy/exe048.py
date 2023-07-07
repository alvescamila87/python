#dicionario de livros com loop

livros = {
    "Dracula": 550,
    "Diário de Anne Frank": 200,
    "Steve Jobs": 300,
    "Star wars III": 150
}

print(livros)

for item in livros:
    print("O livro %s tem %s páginas." %(item, livros[item]))