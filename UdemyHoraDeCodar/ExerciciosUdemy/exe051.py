#funcoes

def return_number(num):
    if num > 10:
        print("The number %d is greater than 10." % num)
    elif num < 10:
        print("The number %d is less than 10." % num)
    else:
        print("The number %d is equal to 10." % num)

return_number(50)
return_number(10)
return_number(5)

#outra forma de fazer o exercicio
a = 3
b = 10
c = 13

def return_number2(num2):
    result = ""

    if num2 > 10:
        result = "greater than 10"
    elif num2 < 10:
        result = "less than 10"
    else:
        result = "equal to 10"

    return result

result_1 = return_number2(a)
print(result_1)

result_2 = return_number2(b)
print(result_2)

result_3 = return_number2(c)
print(result_3)
    