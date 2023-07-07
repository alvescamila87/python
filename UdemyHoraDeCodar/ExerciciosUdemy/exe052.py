#funcoes

def check_size(text):
    if len(text) >= 20:
        print("Large text: %s" % text)
    else:
        print("Short text: %s" % text)

check_size("My name is Camila and I'm 35 yeas old")
check_size("Blumenau is my city")


#outro modo de fazer

def check_tamanho(texto):

    resposta = ""

    if len(texto) >= 20:
        resposta = "Texto muito longo!"
    else:
        resposta = "Texto curto!"

    return resposta

texto_1 = "O rato roeu a roupa do rei de Roma"
resposta_texto_1 = check_tamanho(texto_1)
print(resposta_texto_1)
print(len(texto_1))

texto_2 = "Whatever you want"
resposta_texto_2 = check_tamanho(texto_2)
print(resposta_texto_2)
print(len(texto_2))

print(check_tamanho("Camila"))