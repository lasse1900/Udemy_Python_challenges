string_1 = input("Give me string of integers (comma separated): ")
list_1 = string_1.split(',')
list_out = []
list = set(list_1)

if len(list_1) == 0 or len(list_1) == 1:
    print('None')
else:
    list_out = sorted(list)
    print(list_out[1])
