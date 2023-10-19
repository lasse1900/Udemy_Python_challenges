
string = input("Give a string, I'll print 3 first & 3 last characters: ")

# list = []
# list.append(string)

if len(string) < 6:
    print('')
else:
    s1 = string[:3:]
    start = len(string)-3
    s2 = string[start::]
    s3 = s1 + s2
    print(s3)

# Version B
num_of_chars = 3

if len(string) < 6:
    print('')
else:
    new_string = string[:num_of_chars:] + string[(len(string))-num_of_chars::]
    print(new_string)
