#Data Types: List
#Lists contain regular Python objects, separated by commas and surrounded by brackets. The elements in a list can have any data type, and they can be mixed. 

# list() != my_list = []

#Append: it includes item to list .append()

#Pop: it removes item from a list .pop() or .pop(0)

#Delete: it deletes item or list: del() or del([0])

#Combine or merge lists: 'orignal_list'.extend()

#Remove specific value from a list .remove()

#Remove or clear all item from a list .clear()

#Replace items my_list[0] = 1313

#Length len() or my_list.leng()

#Counting how many times that element is on the list: .count()

#Check if an item is in a list 
my_list = [13, 12, 1987]
if 13 in my_list:
    print('Theres is the number 13 in the list')

#Find the index of an item in a list .index()

#Loop over list elements 'for <element> in <iterable>'
my_list_2 = [55,33,88]
for numbers in my_list:
    print(numbers)

#List to string str() or __str___

#Sorting list: in-place list sort in ascending order: .sort()
#Sorting list: in-place list sort in descending order: .sort(reverse=True)

#Using sorted() ascending, the original list is unchanged
#Using sorted(, reverse=True) descending, the original list is unchanged
