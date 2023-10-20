
string = input("Give a string: ")
cur_char = input("Give character you want to replace from the string: ")
new_char = input("Give the new character: ")
new_string = ''

if string.find(cur_char):
    new_string = string.replace(cur_char, cur_char)
else:
    new_string = string.replace(cur_char, new_char)  

print(new_string)


# ----------------------------------

string = input("Give a string: ")
char_to_replace = input("Give character you want to replace from the string: ")
new_char = input("Give the new character: ")
new_string = ''

for  char in string:
    if char == char_to_replace:
        new_string = new_string + new_char
    else:
        new_string = new_string + char

print(new_string)

