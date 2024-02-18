list_of_items = input("Give a list of items, numbers or alphabet (comma separated): ")
my_list = list_of_items.split(',')
removed_item = input("Give item to be removed: ")
new_list = []

if list_of_items == '':
    print("Empty List")
elif removed_item not in my_list:
    print("Not Found")
else:
    counter = my_list.count(removed_item)

    for char in my_list:
        if char == removed_item:
            # print("char", char, "found and removed")
            continue

        else:
            new_list.append(char)
    print(new_list)

# One liner
# new_list = [item for item in my_list if item != removed_item]


# OR
    
my_list = [3, 3, 2, 1]
elem_to_remove = 3

if not my_list:
	print("Empty List")
elif my_list.count(elem_to_remove) == 0:
	print("Not Found")
else:
	for i in range(my_list.count(elem_to_remove)):
		my_list.remove(elem_to_remove)

print(my_list)

# OR
print("-"*15)

list_of_items = input("Give a list of items, numbers or alphabet (comma separated): ")
my_list = list_of_items.split(',')
removed_item = input("Give item to be removed: ")
new_list = []

new_list = [item for item in my_list if item != removed_item]

print(new_list)