#base de conversao

num = int(input("Digite um número: "))

print('''Escolha uma das bases de conversão: 
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL''')

opcao = int(input("Digite a opção escolhida: "))

if opcao == 1:
    #converter para binário
    #0b (para números binários)
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    #converter para octal
    #0o (para números octais)
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    #converter para hexadecimal
    #0x (para números hexadecimais)
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
elif opcao != [1,2,3]:
    print("Opção inválida. Tente novamente... ")