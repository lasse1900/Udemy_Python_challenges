list_of_items = input("Give a list of items, numbers or alphabet (comma separated): ")

if list_of_items == '':
    print("Empty")
else:
    print("Not Empty")


# OR
    
if len(list_of_items) == 0:
    print("Empty")
else:
    print("Not Empty")

# OR
    
if list_of_items:
    print("Not Empty")
else:
    print("Empty")