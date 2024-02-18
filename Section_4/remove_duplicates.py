list_of_items = input("Give a list of items, numbers or alphabet (comma separated): ")
my_list = list_of_items.split(',')

my_set = set(my_list)

print(sorted(my_set))
