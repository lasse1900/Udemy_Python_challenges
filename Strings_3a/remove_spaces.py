s = input("Give me a string: ")

print(s.replace(" ",""))

new_string = ""
for char in s:
    if char != " ":
        new_string += char

print(new_string)