string_1 = input("Give me string of integers (comma separated, asummed string 1 is shorter than the other string): ")
string_2 = input("Give me another string of integers (comma separated): ")

list_1 = string_1.split(',')
list_2 = string_2.split(',')
list_3 = []

for elem in list_1:
    if elem in list_2:
        list_3.append(elem)

if list_3 == '':
    print('[]')
else:
    print(list_3)