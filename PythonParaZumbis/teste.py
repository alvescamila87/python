# Leitura e gravação de arquivos:

# Função para checar a validade do IP:

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

