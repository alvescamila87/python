#estrutura de repetição: tabuada v3


while True:
    num = int(input("Quer ver a tabuada de qual valor? "))
    print("-"*30)
    if num < 0:
        break
    for c in range(1,11): #tabuada de 1 até 10
        print(f"{num} x {c:2} = {c*num}")
    print("-"*30)
print("PROGRAMA TABUADA ENCERRADO. Volte sempre!")



