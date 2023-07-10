#manipulação de strings: checando se a string é composta por números

numero = "151616165416"
print(numero.isdigit())


numero2 = "2312432.3213"
print(numero2.isdigit())

texto = "kjndflksjnflkndf"
print(texto.isdigit())

#trick para verificar se a frase só tem números
numero3 = "384298347924.8979847392.8794873904"
print(numero3.replace(".", "").isdigit())