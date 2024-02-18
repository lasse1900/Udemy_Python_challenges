string_1 = input("Give me string of integers (comma separated): ")
list_1 = string_1.split(',')
# list_1 = ["a","a","b","c","a","b"]
# list_1 = [1,2,3,4,3,2,1]

dict_1 = {
}

for elem in list_1:
    # print(list_1.count(elem))
    # dict_1.add(elem,list_1.count(elem))
    dict_1[elem] = list_1.count(elem)


print(dict_1)