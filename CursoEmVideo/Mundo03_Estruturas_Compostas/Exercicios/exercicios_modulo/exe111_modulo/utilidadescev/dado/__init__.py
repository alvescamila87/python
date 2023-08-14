def leia_dinheiro(msg):
    ok = False
    valor = 0
    while True:
        p = str(input(msg))
        if p.isnumeric():
            valor = float(p)
            valor = valor.replace(".", ",")
            ok = True
        else:
            print(f"\033[0;31mERRO! '{p}' é um preço inválido!\033[m")
        if ok:
            break
    return valor