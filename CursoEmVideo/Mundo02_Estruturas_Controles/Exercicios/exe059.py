#estrutura de repetição: criando um menu de opções

from time import sleep

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

opcao = 0

while opcao != 5:
    print('''
      [ 1 ] somar
      [ 2 ] multiplicar
      [ 3 ] maior
      [ 4 ] novos números
      [ 5 ] sair do programa
    ''')
    opcao = int(input("Escolha uma das opções: "))

    if opcao == 1:
        soma = num1 + num2
        print("A soma entre {} e {} é: {}.".format(num1, num2, soma))
    elif opcao == 2:
        multiplicacao = num1 * num2
        print("A multiplicação entre {} e {} é: {}.".format(num1, num2, multiplicacao))
    elif opcao == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print("Entre {} e {} o MAIOR é: {}.".format(num1,num2, maior))
    elif opcao == 4:
        print("Informe os números novamente:")
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
    elif opcao == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente!")
    print('=-='*10)
sleep(2)
print("Fim do programa! Volte sempre!")



