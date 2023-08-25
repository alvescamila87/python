
#Opção 1 - Gravação
f = open(r'c:/Users/Camila/OneDrive/GitHub/python/PythonParaZumbis/file.txt', 'w')
for linha in range(1, 101):
    f.write(f"{linha}\n")
f.close()

#Opção 2 - Leitura 1
f = open(r'c:/Users/Camila/OneDrive/GitHub/python/PythonParaZumbis/file.txt')
for linha in f.readlines():
    print(linha.strip())
f.close()

#Opção 3 - Leitura 2
with open(r"c:/Users/Camila/OneDrive/GitHub/python/PythonParaZumbis/file.txt") as f:
    print(f.read())
# 4) Leitura e gravação de arquivos:

texto = open('c:/Users/Camila/OneDrive/GitHub/python/PythonParaZumbis/mensagem.txt', 'r')
cripto = open('c:/Users/Camila/OneDrive/GitHub/python/PythonParaZumbis/cripto.txt', 'w')

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


arq = open('c:/Users/Camila/OneDrive/GitHub/python/PythonParaZumbis/IPS.txt')
validos = open('c:/Users/Camila/OneDrive/GitHub/python/PythonParaZumbis/IPS_validos.txt', 'w')
invalidos = open('c:/Users/Camila/OneDrive/GitHub/python/PythonParaZumbis/IPS_invalidos.txt', 'w')

for linha in arq.readlines():
    if ip_ok(linha):
        validos.write(linha)
    else:
        invalidos.write(linha)

arq.close()
validos.close()
invalidos.close()