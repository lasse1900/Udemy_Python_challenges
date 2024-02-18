string_1 = input("Give me string of integers (comma separated): ")
string_2 = input("Give me another string of integers (comma separated): ")

list_1 = string_1.split(',')
list_2 = string_2.split(',')
list_3 = []

if (string_1) == '':
    print('[]')
elif (list_1 == list_2):
    print('[same]')
else:
    for elem in list_1:
        if elem in list_2:
            continue
        else:
            list_3.append(elem)
    print(list_3)


# OR
    
listA = [1, 2, 3, 4]
listB = [1, 2]

difference = []

for elem in listA:
	if elem not in listB:
		difference.append(elem)

print(difference)