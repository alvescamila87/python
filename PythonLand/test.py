door_is_locked = False
if door_is_locked:
    print('Mum, open the door, please.')
else:
    print("Let's go inside!")

for letter in 'Hello':
    print(letter)

mylist = ['Camila', 35, 'Paulo', 63, 'Bela', 61, 'Karoline', 36]
for items in mylist:
    print(items)
    print(mylist[4])
    print(mylist[3] + mylist[1])


i = 0
while i <= 4:
    print(i)
    i = i + 1

def say_hi():
    print('Hi')

say_hi()

def greeter(name, location):
    print('Hi', name, 'welcome to', location)

greeter('Camila', 'Blumenau')

def add(a, b):
    return a + b

result = add(4, 8)
print(result)

def optional_greeter(name):
    if name.startswith('X'):
        #We don't greet people with wierd names :P
        return

    print('Hi there, ', name)

optional_greeter('Xander')

def say_hello():
    print('Hi', name)

name = 'Camila'
say_hello()

def welcome(name="Bella", location='Blumenau'):
    print('Hi,', name, 'welcome to', location)

welcome()
welcome('Camila')
welcome(name='Karoline', location='Timbó')