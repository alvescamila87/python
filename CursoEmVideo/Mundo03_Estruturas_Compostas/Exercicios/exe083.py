#estruturas compostas: Validando expressões matemáticas

expressao = str(input("Digite a expressão: "))
pilha = []
for simbolo in expressao:
    # Verifica se a lista da pilha está cheia ou vazia
    if simbolo == '(':
        pilha.append("(")
    elif simbolo == ')':
        if len(pilha) > 0: # Verifica se a pilha NÃO está vazia
            pilha.pop() # Remove o último elemento
        else: # Se a pilha estiver vazia
            pilha.append(')') # Sinal de que teve mais parênteses fechando que abrindo
            break
if len(pilha) == 0: # Cada parênteses que abriu, teve sua relação com parênteses fechando
    print(f"Sua expressão está VÁLIDA: {expressao}")
else: 
    print(f"Sua expressão está I-N-VÁLIDA: {expressao}")