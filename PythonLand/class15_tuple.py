#Data Types: Tuple

# Unacking trick 

>>> l1 = [1, 2, 3]
>>> l2 = [4, 5, 6]
>>> t = (*l1, *l2)
>>> t
(1, 2, 3, 4, 5, 6)


# Multiple assigning using a python tuple

>>> person = ('Camila', 35, True)
>>> name, age, registered = person
>>> name
"Camila"
>>> 

def get_user_by_id(userid):
    # fetch user from database
    # ....
    return name, age
 
name, age = get_user_by_id(4)

#index access [0]

#apend: extra items: create a new tuple with the unpacked values and two different strings and assign the result to t again.

#get a len() from tuple

#converting tuple to list: list()

#converting tuple to string: str()