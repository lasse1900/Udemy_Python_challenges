list_of_items = input("Give a list of numbers (comma separated): ")
my_list = list_of_items.split(',')
counter = 0

if list_of_items == '':
    print(counter)
else:
    for i in my_list:
        if int(i) > 3:
            counter += 1

    print(counter)

    
# OR one liner
my_list = [1, -1, 0, 2, 2, 3, 4, 5]
count = 0
count = sum(1 for elem in my_list if elem > 3)
print(count)