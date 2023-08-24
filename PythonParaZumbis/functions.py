# funcao fatorial

def fatorial(n):
    f = 1
    while n > 0:
        f = f * n
        n = n - 1
    return f

print(fatorial(5))

# 6) for == while enrustido - exe04 - fatorial

for i in range(5):
    print(fatorial(i))