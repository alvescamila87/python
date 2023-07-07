#funcao que retorna números pares de lista

list_1 = [1,2,3,4,5,6,7,8,9,10]

def return_pair(list_1):

    list_2 = []

    for x in list_1:
        if x % 2 == 0:
            list_2.append(x)

    return list_2
              
pair_list = return_pair(list_1)

print(pair_list)

#funcao que retorna números ímpares de lista

list_3 = [10,20,30,40,50,60,70,80,90,105,115,125,135,802,906,1002]

def return_odd(list_3):

    list_4 = []

    for y in list_3:
        if y % 2 != 0:
            list_4.append(y)

    return list_4

odd_list = return_odd(list_3)
print(odd_list)

