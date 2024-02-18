list_of_items = input("Give a list of items, numbers or alphabet (comma separated): ")
my_list = list_of_items.split(',')

if list_of_items == '':
    print("Empty List")
else:
    for i, char in enumerate(my_list):
	    print(char, i)

