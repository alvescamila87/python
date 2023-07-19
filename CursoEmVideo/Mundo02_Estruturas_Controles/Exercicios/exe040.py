#Média de nota da matéria

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))

media = (nota1 + nota2) / 2

if media < 5:
    print("Tirando {} e {} a média do aluno é {}.".format(nota1, nota2, media))
    print("REPROVADO!")
elif media <= 6.9 and media >= 5:
    print("Tirando {} e {} a média do aluno é {}.".format(nota1, nota2, media))
    print("RECUPERAÇÃO!")
elif media > 7:
    print("Tirando {} e {} a média do aluno é {}.".format(nota1, nota2, media))
    print("APROVADO!")
