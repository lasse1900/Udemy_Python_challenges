
string = input("Give a string, I'll remove characters at even indices: ")
new_string = ''
new_string_2 = ''
if (len(string) == 0 or len(string) == 1):
    print(string)

for i in range(len(string)):
    if(i % 2 != 0):
        # print(string[i], end="")
        new_string += string[i]

print(new_string)


for i in range(1, len(string),2):
    new_string_2 += string[i]

print(new_string_2)