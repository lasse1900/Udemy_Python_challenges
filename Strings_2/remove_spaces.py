
given_s = input("Give a string - I'll remove spaces: ")
new_string = ''

for char in given_s:
    if char == " ":
        pass
    else:
        new_string += char

print(new_string)

print('-'*20)

print(given_s.replace(" ",""))