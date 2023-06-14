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

def greet(name, location):
    print('Hi', name, 'welcome to', location)

greet('Camila', 'Blumenau')


