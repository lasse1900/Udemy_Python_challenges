s = input("Give me a string: ")

if len(s) <= 1:
    print(s)
else:
    print(s[1::2])

# OR
    
new_string = ""
for i in range (1, len(s), 2):
    new_string += s[i]

if len(s) <= 1:
    print(s)
else:
    print(new_string)