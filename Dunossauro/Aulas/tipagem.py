# atribuição multipla
# não precisa usar os temporários 'aux'
a = 3
b = 'abacate'

print("ANTES da atribuição múltipla: A = ",a," B = ", b)

a, b = b, a

print("DEPOIS da atribuição múltipla: A = ", a," 'B = ", b)