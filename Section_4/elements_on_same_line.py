list_of_items = input("Give a list of items, numbers or alphabet (comma separated): ")

short_list = list_of_items.split(',')

print(short_list)
char_list = ''

for char in short_list:
    char_list += char + ' '


print(char_list)