
#Opção 1 - Gravação
f = open(r'c:/Users/Camila/Downloads/file.txt', 'w')
for linha in range(1, 101):
    f.write(f"{linha}\n")
f.close()

#Opção 2 - Leitura 1
f = open(r'c:/Users/Camila/Downloads/file.txt')
for linha in f.readlines():
    print(linha.strip())
f.close()

#Opção 3 - Leitura 2
with open(r"c:/Users/Camila/Downloads/file.txt") as f:
    print(f.read())
# 4) Leitura e gravação de arquivos:

texto = open('c:/Users/Camila/Downloads/mensagem.txt', 'r')
cripto = open('c:/Users/Camila/Downloads/cripto.txt', 'w')

for linha in texto.readlines():
    for letra in linha:
        if letra in 'aeiouãõ':
            cripto.write("*")
        else:
            cripto.write(letra)

texto.close()
cripto.close()

# 5) # Leitura e gravação de arquivos com função para checar a validade do IP:

def ip_ok(ip):
    ip = ip.split('.')
    for byte in ip:
        if int(byte) > 255:
            return False
    return True


arq = open('c:/Users/Camila/Downloads/IPS.txt')
validos = open('c:/Users/Camila/Downloads/IPS_validos.txt', 'w')
invalidos = open('c:/Users/Camila/Downloads/IPS_invalidos.txt', 'w')

for linha in arq.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)

arq.close()
validos.close()
invalidos.close()