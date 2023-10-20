
string = input("Give a string: ")
index = int(input("Give index of the character you want delete: "))
new_string = ''

if (index > len(string) or string == ''): # if (index > len(string) or (not string)): # Alternative
    print(string)
else:
    for i in range(len(string)):
        if i != index:
            new_string += string[i]

print(new_string)

