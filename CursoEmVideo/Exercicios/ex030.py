n=int(input('informe um número: '))
if n/2 == 0:
    print('O número {} é \033[34mpar\033[m.'.format(n))
else:
    print('O número {} é impar'.format(n))