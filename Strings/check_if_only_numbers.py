
string = input("Give a string - I'll check if the string has only numbers: ")
output = 'False'
for i in range(len(string)):
    if len(string) == 0:
        output = False
        break
    elif string[i].isdigit() == True:
        output = True
    elif string[i].isdigit() == False:
        output = False
        break

print(output)
print('-'*15)
print(string.isdecimal())