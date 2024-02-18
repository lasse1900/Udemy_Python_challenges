list_of_items = input("Give a list of items, numbers or alphabet (comma separated): ")

list = list_of_items.split(',')

if list_of_items == '':
    print("[]")

if (int(max(list)) and int(min(list))) < 0:
    print(min(list),max(list))
else:
    print(max(list),min(list))


# OR

# my_list = [3, 4, 5, 6]
my_list = [-1,-2,-3,-4]

if my_list:
	print(max(my_list), min(my_list))
else:
	print(None)
      
