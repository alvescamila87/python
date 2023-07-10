#manipulação de strings: contando o número de ocorrências: count

frase = "Essa é a frase que vamos checar as ocorrências da palavra frase"

#count para verificar a qtd de vezes que palavra "frase" ocorre:
print(frase.count("frase"))

if frase.count("frase") == 2:
    print("A contagem está correta!")

#quando não possui ocorrência da palavra:
print(frase.count("olá"))

