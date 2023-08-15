# Tratamento de erros e exceções
# Erro de sintaxe ou erro semântico (erro de exceção)
# Python exception list
# Utilizando estrututa: try (operação), except (falhou), else (deu certo), finally (certo/falha)

# 1) Tratamento de erro:
# else e finally são OPCIONAIS
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except:
    print("Infelizmente tivemos um problema :(")
else:
    print(f"O resultado é {r:.1f}.")
finally:
    print("Volte sempre! Muito obrigada! ")


# 2) Classificar o erro:
try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except Exception as erro:
    print(f"Problema encontrado foi {erro.__class__}")
else:
    print(f"O resultado é {r:.1f}.")
finally:
    print("Volte sempre! Muito obrigada! ")

# 3) Try pode ter vários excepts, ou seja, tipos de classificação de erro:
# Exemplo: except TypeError, except ValueError, except OSError

try:
    a = int(input("Numerador: "))
    b = int(input("Denominador: "))
    r = a / b
except (ValueError, TypeError):
    print("Tivemos um problema com os tipos de dados que você digitou.")
except ZeroDivisionError:
    print("Não é possível dividir um número por zero!")
except KeyboardInterrupt:
    print("O usuário preferiu não informar os dados!")
except Exception as erro:
    # Para tratamento de erros genéricos:
    print(f"O erro encontrado foi {erro.__cause__}")
else:
    print(f"O resultado é: {r:.1f}")
finally:
    print("Volte sempre! :)")
