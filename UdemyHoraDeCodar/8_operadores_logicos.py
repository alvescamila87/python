# not and or

#not
verdadeiro = True
falso = False

print(not verdadeiro)
print(not falso)
print(not (5 > 2))

#and
a = 5
b = 10
c = 2
d = 8

print(a > b and c > d) #false
print(a > b and c < d) #false
print(c < d and d < c) #false
print(a < b and b > c) #true

#or
a = 5
b = 10

print(a > b or b == 11) #false
print(b > a or b == 10) #true
print(a > b or b == 20) #false

nome = "Paulo"
idade = 61

print(nome == 'Joao' or idade >= 18) #true
