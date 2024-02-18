list_of_items = input("Give a list of items, numbers or alphabet (comma separated): ")
factor = int(input("Give me the factor: "))

short_list = list_of_items.split(',')
print(len(short_list))
counter = 0

print(short_list)
for item in short_list:
    counter += 1
    if item.isnumeric():
        item = int(item)
        if (item != ' ') or (item != ','):
            item = int(item) * factor
        if(counter == len(short_list)):
            print(item, end='')
        else:
            print(item, end=',')
    elif item.isnumeric() == False:
        if (item != ' ') or (item != ','):
            item = item * factor
        if(counter == len(short_list)):
            print(item, end='')
        else:
            print(item, end=',')


# OR
print()            
            
my_list = [3, 4, 5, 6]
factor = 2

for i in range(len(my_list)):
	my_list[i] *= factor

print(my_list)

# OR

# my_list = [3, 4, 5, 6]
my_list = ['a','b','c']
factor = 2

for i, elem in enumerate(my_list):
	my_list[i] = elem * factor

print(my_list)

