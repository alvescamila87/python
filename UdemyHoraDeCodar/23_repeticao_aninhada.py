#while dentro de while

x = 0

while x < 10:
    print("x é: %d" % x)

    y = 0
    
    while y < 5:
        print("y é: %d" %y)
        y = y + 1

    x = x + 1 