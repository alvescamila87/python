# Exception: EXERCÍCIO Verificar acessibilidade de site

# Opção Camila
import webbrowser

def acessa_site(site):
    try:
        webbrowser.open(site)
    except:
        print("Deu ERRO!")
    else:
        print("Tudo Ok!")


site = acessa_site("http://pudim.com.br")

# Opção Guanabara

import urllib
import urllib.request

try:
    site = urllib.request.urlopen("http://pudim.com.br")
except urllib.error.URLError:
    print("O site pudim não esta acessível no momento.")
else:
    print("Consegui acessar o site Pudim com sucesso!")










