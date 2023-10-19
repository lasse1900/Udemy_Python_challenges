
string = input("Give a string: ")
print(string[::-1])
reversed_string = string[::-1]

for i in range(int(len(string))):
    print(string[len(string)-i-1], end='')

print('\n-----------')

string = input("Give a string: ")

string = ''.join(reversed(string))
print(string)