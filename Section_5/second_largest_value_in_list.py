string_1 = input("Give me string of integers (comma separated): ")

list_1 = string_1.split(',')


list_out = []
list = set(list_1)

if len(list_1) == 0 or len(list_1) == 1:
    print('None')
else:
    list_out = sorted(list)
    print(list_out[len(list_out)-2])

# OR
    
my_list = [1, 2, 3, 4]

if len(my_list) > 1:
	no_duplicates = set(my_list)
	no_duplicates.remove(max(no_duplicates))
	print(max(no_duplicates)) 
else:
	print(None)
