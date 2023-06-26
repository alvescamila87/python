#Data Types: Floating point number
#A floating-point number is a number with a decimal point or exponent notation, indicating that a number is a certain number of digits before and after the decimal point or exponent.


f = 1.45e3
float(f)
print(f)

#round()
f = 3.5904590
round(f, 5)
print(f)

#floor and ceil (need to import from math library)

from math import floor, ceil
# Round 1.23 down to the nearest integer
x = floor(1.23)  # x will be 1
# Round 1.23 up to the nearest integer
y = ceil(1.23)  # y will be 2

#comparison
x = 1.23
y = 4.56
if x == y:
    print("x and y are equal")
else:
    print("x and y are not equal")


#NumPy: 
#The numpy module is a popular scientific computing library for Python that supports working with arrays of numbers.