#manipulação de strings: pesquisando palavras: in e not in

frase = "O rato roeu a roupa do rei de Roma"

if "rato" in frase:
    print("Encontramos a palavra 'rato' na frase")
else:
    print("Tente outra palavra da frase, pois essa não foi encontrada")

print("rato" in frase)

if "Camila" not in frase:
    print("Não encontramos esse nome na frase")
else:
    print("Encontramos o nome na frase.")
    
print("Camila" not in frase)