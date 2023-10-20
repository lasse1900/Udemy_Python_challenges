
string = input("Give a string - I'll change commas to dots: ")
new_string = ''

for char in string:
    if char == ',':
        new_string = string.replace(char, '.')

print(new_string)


# ----------------------------------
new_string_2 = ''
print('-'*15)
new_string_2 = string.replace(',', '.')
print(new_string_2)
