# First Program
# - input(): ask for input and assign that input to a variable.

def say_hi(name):
    if name == '':
        print("You didn't enter your name!")
    else:
        print("Hi there...")

    for letter in name:
        print(letter)

# This is an infinite loop
while True:
    # Ask for the first name using input()
    name = input('Type your name: ')
    # And then call say_hi with the name
    say_hi(name)

###

def say_hi(name):
    if name == '' or len(name) <=1:
        print("You didn't enter your name!")
    else:
        print('Hey, there...')

    for letter in name:
        print(letter)

while True:
    name = input('Your name: ')
    say_hi(name)

